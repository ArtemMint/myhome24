from django.db import models


class Flat(models.Model):
    number = models.CharField(
        max_length=50,
        verbose_name='Номер квартиры',
        blank=False,
        null=True,
    )
    area = models.FloatField(
        max_length=50,
        verbose_name='Площадь(кв.м.)',
        blank=True,
        null=True,
    )
    house = models.ForeignKey(
        'admin_panel.House',
        on_delete=models.CASCADE,
        related_name='flats',
        verbose_name='Дом',
        null=True,
        blank=False,
    )
    section = models.ForeignKey(
        'admin_panel.HouseSection',
        on_delete=models.CASCADE,
        related_name='flats',
        verbose_name='Секция',
        null=True,
        blank=True,
    )
    floor = models.ForeignKey(
        'admin_panel.HouseFloor',
        on_delete=models.CASCADE,
        related_name='flats',
        verbose_name='Этаж',
        null=True,
        blank=True,
    )
    owner = models.ForeignKey(
        'register.User',
        on_delete=models.CASCADE,
        related_name='flats',
        verbose_name='Владелец',
        null=True,
        blank=True,
    )
    tariff = models.ForeignKey(
        'admin_panel.Tariff',
        on_delete=models.CASCADE,
        related_name='flats',
        verbose_name='Тариф',
        null=True,
        blank=True,
    )
    account = models.ForeignKey(
        'admin_panel.Account',
        on_delete=models.CASCADE,
        related_name='flats',
        verbose_name='Лицевой счет',
        null=True,
        blank=True,
    )
    created_date = models.DateTimeField(
        auto_now_add=True,
    )
    editing_date = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return f'№{self.number} - {self.house}'

    class Meta:
        ordering = ('-editing_date',)

    @classmethod
    def get_flats_count(cls):
        return cls.objects.all().count()

    @classmethod
    def get_flats_list(cls):
        return cls.objects.all()

    @classmethod
    def get_flat_by_pk(cls, pk):
        return cls.objects.get(pk=pk)
