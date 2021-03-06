# Generated by Django 3.2.13 on 2022-06-26 05:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Room",
            fields=[
                (
                    "number",
                    models.PositiveIntegerField(primary_key=True, serialize=False),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("A", "availabe"), ("R", "reserved")],
                        default="A",
                        max_length=1,
                    ),
                ),
                (
                    "room_type",
                    models.CharField(
                        choices=[
                            ("small", "Small"),
                            ("big", "Big"),
                            ("large", "Large"),
                            ("sweet", "Sweet"),
                        ],
                        default="small",
                        max_length=5,
                    ),
                ),
                ("image", models.ImageField(blank=True, upload_to="rooms/images")),
            ],
            options={
                "ordering": ["number"],
            },
        ),
        migrations.CreateModel(
            name="Reservation",
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
                (
                    "bill_status",
                    models.CharField(
                        choices=[("P", "Pending"), ("C", "Complete"), ("F", "Failed")],
                        default="P",
                        max_length=1,
                    ),
                ),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "room",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="hotel.room"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
