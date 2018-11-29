# Generated by Django 2.0 on 2018-11-29 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='logo',
            field=models.ImageField(upload_to='logo/%Y/%m', verbose_name='封面图'),
        ),
        migrations.AlterField(
            model_name='movies',
            name='url',
            field=models.FileField(upload_to='movies/%Y/%m', verbose_name='资源文件'),
        ),
    ]
