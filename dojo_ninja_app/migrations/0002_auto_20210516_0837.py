# Generated by Django 2.2 on 2021-05-16 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninja_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dojos',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='dojos',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='dojos',
            name='desc',
            field=models.TextField(default=''),
        ),
    ]
