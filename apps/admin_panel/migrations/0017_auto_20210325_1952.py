# Generated by Django 3.1.7 on 2021-03-25 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0016_auto_20210324_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutextrainfo',
            name='about',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='extra_info', to='admin_panel.aboutpage'),
        ),
    ]
