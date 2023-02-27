# Generated by Django 4.1.5 on 2023-02-27 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0007_alter_player_time"),
    ]

    operations = [
        migrations.CreateModel(
            name="Ques",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("ans", models.CharField(max_length=200, null=True)),
                (
                    "direction",
                    models.CharField(
                        choices=[("across", "across"), ("down", "down")],
                        max_length=200,
                        null=True,
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="QuesModel",
        ),
    ]