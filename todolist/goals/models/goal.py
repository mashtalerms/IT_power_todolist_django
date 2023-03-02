from django.db import models

from goals.models.base import DatesModelMixin
from goals.models.board import Board
from core.models import User


class Goal(DatesModelMixin):

    class Meta:
        app_label = "goals"
        verbose_name = "Цель"
        verbose_name_plural = "Цели"


    class Status(models.IntegerChoices):
        to_do = 1, "К выполнению"
        in_progress = 2, "В процессе"
        done = 3, "Выполнено"
        archived = 4, "Архив"

    class Priority(models.IntegerChoices):
        low = 1, "Низкий"
        medium = 2, "Средний"
        high = 3, "Высокий"
        critical = 4, "Критический"

    title = models.CharField(verbose_name="Заголовок", max_length=255)
    description = models.CharField(verbose_name="Описание", max_length=500, null=True)
    due_date = models.DateField(verbose_name="Дата выполнения", null=True)
    status = models.PositiveSmallIntegerField(
        verbose_name="Статус", choices=Status.choices, default=Status.to_do
    )
    priority = models.PositiveSmallIntegerField(
        verbose_name="Приоритет", choices=Priority.choices, default=Priority.medium
    )
    user = models.ForeignKey(User, verbose_name="Автор", on_delete=models.PROTECT)
    board = models.ForeignKey(Board, verbose_name="Категория", on_delete=models.CASCADE)
    is_deleted = models.BooleanField(verbose_name="Удалена", default=False)
