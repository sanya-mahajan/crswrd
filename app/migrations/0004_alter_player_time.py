# Generated by Django 4.1.5 on 2023-02-01 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0003_remove_quesmodel_question_alter_quesmodel_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="player",
            name="time",
            field=models.TimeField(blank=True, null=True),
        ),
    ]
