from django.db import transaction #TODO

from rest_framework import serializers

from core.models import User
from goals.models.board import Board

from ..models.partisipant import BoardParticipant


class BoardCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Board
        read_only_fields = ("id", "created", "updated")
        fields = "__all__"

    def create(self, validated_data):
        user = validated_data.get("user")
        board = Board.objects.create(**validated_data)
        BoardParticipant.objects.create(
            user=user, board=board, role=BoardParticipant.Role.owner
        )
        return board


class BoardListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = "__all__"


class BoardParticipantSerializer(serializers.ModelSerializer):
    role = serializers.ChoiceField(
        required=True, choices=BoardParticipant.Role
    )
    user = serializers.SlugRelatedField(
        slug_field="email", queryset=User.objects.all()
    )

    class Meta:
        model = BoardParticipant
        fields = "__all__"
        read_only_fields = ("id", "created", "updated", "board")


class BoardSerializer(serializers.ModelSerializer):
    participants = BoardParticipantSerializer(many=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Board
        fields = "__all__"
        read_only_fields = ("id", "created", "updated")

    def update(self, instance, validated_data):
        if validated_data.get("participants"):
            new_participants = validated_data.pop("participants")
            new_by_id = {part["user"].id: part for part in new_participants}

            old_participants = instance.participants.exclude(user=self.context.get('request').user)
            with transaction.atomic():
                for old_participant in old_participants:
                    if old_participant.user_id not in new_by_id:
                        old_participant.delete()
                    else:
                        if (
                                old_participant.role
                                != new_by_id[old_participant.user_id]["role"]
                        ):
                            old_participant.role = new_by_id[old_participant.user_id][
                                "role"
                            ]
                            old_participant.save()
                        new_by_id.pop(old_participant.user_id)
                for new_part in new_by_id.values():
                    BoardParticipant.objects.create(
                        board=instance, user=new_part["user"], role=new_part["role"]
                    )

        instance.title = validated_data.get("title", instance.title)
        instance.save()

        return instance
