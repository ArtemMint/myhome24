# Generated by Django 3.1.7 on 2021-03-23 18:57

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0009_auto_20210323_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indexblock',
            name='index',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blocks', to='admin_panel.indexpage', verbose_name='Title of the block'),
        ),
        migrations.AlterField(
            model_name='indexslider',
            name='index',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slider', to='admin_panel.indexpage'),
        ),
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('short_text', ckeditor.fields.RichTextField(max_length=1000)),
                ('image', models.ImageField(upload_to='images/about/director/', verbose_name='Recommend size (250x310)')),
                ('seo', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_panel.seo', verbose_name='Settings SEO')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AboutGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images/about/gallery/', verbose_name='Recommend size (1200x1200)')),
                ('about', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='admin_panel.aboutpage')),
            ],
        ),
        migrations.CreateModel(
            name='AboutExtraInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('short_text', ckeditor.fields.RichTextField(max_length=1000)),
                ('about', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='extra_info', to='admin_panel.aboutpage')),
            ],
        ),
        migrations.CreateModel(
            name='AboutExtraGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images/about/additional_gallery/', verbose_name='Recommend size (1200x1200)')),
                ('about', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='extra_gallery', to='admin_panel.aboutpage')),
            ],
        ),
        migrations.CreateModel(
            name='AboutDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='files/about/', verbose_name='PDF, JPG (max.size 20 Mb)')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Name of the document')),
                ('about', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='admin_panel.aboutpage')),
            ],
        ),
    ]
