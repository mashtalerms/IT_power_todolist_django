from django.db import models

from goals.models.base import DatesModelMixin

from core.models import User


class Board(DatesModelMixin):
    class Meta:
        verbose_name = "Доска"
        verbose_name_plural = "Доски"
        app_label = "goals"

    title = models.CharField(verbose_name="Название", max_length=255)
    is_deleted = models.BooleanField(verbose_name="Удалена", default=False)
    user = models.ForeignKey(User, verbose_name="Автор", on_delete=models.PROTECT, default=None)
