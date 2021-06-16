from django.db import models


class HouseUserAdmin(models.Model):
    house = models.ForeignKey(
        'admin_panel.House',
        on_delete=models.CASCADE,
        related_name='house_user_admin',
        default=None,
    )
    user_admin = models.ForeignKey(
        'register.User',
        on_delete=models.SET_NULL,
        verbose_name="ФИО",
        related_name='house_user_admin',
        blank=True,
        null=True,
    )
    created_date = models.DateTimeField(
        auto_now_add=True,
    )
    editing_date = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return f'{self.user_admin}'

    @classmethod
    def get_user_admin_list(cls, pk):
        return cls.objects.filter(house=pk)
