# Generated by Django 3.1.7 on 2021-05-12 08:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admin_panel', '0021_auto_20210511_2154'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='flat',
            options={'ordering': ('house',)},
        ),
        migrations.AlterField(
            model_name='flat',
            name='floor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='flats', to='admin_panel.housefloor'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='house',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='flats', to='admin_panel.house'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='flats', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='flat',
            name='section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='flats', to='admin_panel.housesection'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='tariff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='flats', to='admin_panel.tariff'),
        ),
    ]
