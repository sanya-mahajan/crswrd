# Generated by Django 4.1.5 on 2023-02-01 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_player"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="quesmodel",
            name="question",
        ),
        migrations.AlterField(
            model_name="quesmodel",
            name="id",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]