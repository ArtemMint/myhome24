# Generated by Django 3.1.7 on 2021-05-25 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0036_auto_20210525_1835'),
    ]

    operations = [
        migrations.CreateModel(
            name='HouseUserAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='ФИО')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('editing_date', models.DateTimeField(auto_now=True)),
                ('house', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='house_user_admin', to='admin_panel.house')),
            ],
        ),
    ]
