# Generated by Django 3.2 on 2022-04-25 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserveapp', '0002_reservemodel2'),
    ]

    operations = [
        migrations.DeleteModel(
            name='reservemodel',
        ),
        migrations.AlterField(
            model_name='reservemodel2',
            name='category',
            field=models.CharField(max_length=50, verbose_name='予約可能部屋'),
        ),
    ]
