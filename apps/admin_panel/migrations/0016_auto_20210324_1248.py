# Generated by Django 3.1.7 on 2021-03-24 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0015_auto_20210324_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutpage',
            name='seo',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='about_page', to='admin_panel.seo', verbose_name='Setting SEO'),
        ),
    ]
