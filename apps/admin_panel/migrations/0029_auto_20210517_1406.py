# Generated by Django 3.1.7 on 2021-05-17 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0028_auto_20210516_1753'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='account_balance',
            new_name='balance',
        ),
    ]
