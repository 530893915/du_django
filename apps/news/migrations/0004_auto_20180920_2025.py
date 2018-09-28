# Generated by Django 2.0.5 on 2018-09-20 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20180918_1418'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_h3', models.CharField(max_length=20)),
                ('title_p', models.CharField(max_length=40)),
                ('image_url', models.URLField()),
                ('priority', models.IntegerField(default=0)),
                ('link_to', models.URLField()),
                ('pub_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-pub_time']},
        ),
        migrations.AlterField(
            model_name='comment',
            name='news',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commands', to='news.News'),
        ),
    ]
