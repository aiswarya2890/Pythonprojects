# Generated by Django 4.1 on 2022-09-03 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2000-11-10'),
            preserve_default=False,
        ),
    ]
