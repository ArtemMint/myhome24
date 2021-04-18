# Generated by Django 3.1.7 on 2021-03-26 14:50

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0017_auto_20210325_1952'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicesPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images/services/', verbose_name='Recommend size (650x300)')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('description', ckeditor.fields.RichTextField(blank=True, max_length=1000)),
                ('seo', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='services_page', to='admin_panel.seo', verbose_name='Settings SEO')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
