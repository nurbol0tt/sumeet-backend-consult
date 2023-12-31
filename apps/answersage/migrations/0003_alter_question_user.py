# Generated by Django 4.2.4 on 2023-08-12 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0002_alter_consultant_user"),
        ("answersage", "0002_alter_question_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="consultations",
                to="user.user",
            ),
        ),
    ]
