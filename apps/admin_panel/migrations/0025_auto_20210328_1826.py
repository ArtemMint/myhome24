# Generated by Django 3.1.7 on 2021-03-28 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0024_auto_20210328_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seo',
            name='seo_description',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='seo',
            name='seo_keywords',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='seo',
            name='seo_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
