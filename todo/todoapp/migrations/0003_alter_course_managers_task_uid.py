# Generated by Django 4.0.5 on 2022-08-09 06:49

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_course'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='course',
            managers=[
                ('ccustomobj', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='uid',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
