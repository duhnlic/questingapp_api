# Generated by Django 3.2 on 2021-04-27 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quests', '0009_auto_20210427_0310'),
    ]

    operations = [
        migrations.AddField(
            model_name='quest',
            name='kind',
            field=models.CharField(default='questing', max_length=100),
        ),
    ]
