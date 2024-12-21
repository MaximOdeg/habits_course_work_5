# Generated by Django 5.1.4 on 2024-12-21 07:10

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Habit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("habit", models.CharField(max_length=255, verbose_name="Привычка")),
                (
                    "place_of_execution",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Место где нужно выполнять привычку",
                    ),
                ),
                (
                    "time_execution",
                    models.TimeField(
                        blank=True,
                        null=True,
                        verbose_name="Время когда выполняется привычка",
                    ),
                ),
                (
                    "periodicity",
                    models.PositiveSmallIntegerField(
                        default=1,
                        validators=[django.core.validators.MaxValueValidator(7)],
                        verbose_name="Периодичность привычки",
                    ),
                ),
                (
                    "time_to_complete",
                    models.DurationField(
                        default=datetime.timedelta(seconds=120),
                        verbose_name="Продолжительность выполнения привычки по времени",
                    ),
                ),
                (
                    "sign_of_a_pleasant_habit",
                    models.BooleanField(
                        default=False, verbose_name="Показатель приятной привычки"
                    ),
                ),
                (
                    "reward",
                    models.CharField(
                        blank=True, null=True, verbose_name="Вознаграждение за привычку"
                    ),
                ),
                (
                    "published",
                    models.CharField(
                        choices=[
                            ("Опубликован", "Опубликован"),
                            ("Не опубликован", "Не опубликован"),
                        ],
                        default="Не опубликован",
                        max_length=50,
                        verbose_name="Статус опубликования привычки",
                    ),
                ),
                (
                    "send_indicator",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        editable=False,
                        null=True,
                        verbose_name="Индикатор отправки",
                    ),
                ),
            ],
            options={
                "verbose_name": "Привычка",
                "verbose_name_plural": "Привычки",
                "ordering": ("id",),
            },
        ),
    ]
