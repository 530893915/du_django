# Generated by Django 2.0.5 on 2018-09-27 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_courseorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseorder',
            name='istype',
            field=models.SmallIntegerField(default=0),
        ),
    ]