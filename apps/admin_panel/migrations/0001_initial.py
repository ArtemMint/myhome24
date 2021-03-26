# Generated by Django 3.1.7 on 2021-03-22 10:48

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IndexPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('short_text', ckeditor.fields.RichTextField(max_length=1000)),
                ('apps_status', models.BooleanField(default='False', verbose_name='Show apps links')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SEO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=150, null=True)),
                ('keywords', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IndexSlider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images/index/slider/')),
                ('index', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.indexpage')),
            ],
        ),
        migrations.AddField(
            model_name='indexpage',
            name='seo',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='admin_panel.seo', verbose_name='Settings SEO'),
        ),
        migrations.CreateModel(
            name='IndexBlocks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/index/near_us/')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('index', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.indexpage')),
            ],
        ),
    ]
