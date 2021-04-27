# Generated by Django 3.2 on 2021-04-27 03:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quests', '0008_auto_20210423_1904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quest',
            name='active_user',
        ),
        migrations.AlterField(
            model_name='quest',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quest', to='quests.user'),
        ),
    ]
