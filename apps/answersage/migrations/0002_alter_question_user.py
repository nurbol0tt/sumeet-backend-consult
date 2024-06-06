# Generated by Django 4.2.4 on 2023-08-12 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0001_initial"),
        ("answersage", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="consultations",
                to="user.user",
            ),
        ),
    ]