from django.contrib import admin

from goals.models.board import Board
from goals.models.goal import Goal


class BaseAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "created", "updated")
    search_fields = ("title", "user")
    readonly_fields = ("created", "updated")


class GoalAdmin(BaseAdmin):
    list_display = ("title", "user", "created", "updated")
    search_fields = ("title", "user")


class BoardAdmin(BaseAdmin):
    list_display = ("title", "created", "updated", "user")
    search_fields = ("title",)


admin.site.register(Goal, GoalAdmin)
admin.site.register(Board, BoardAdmin)
