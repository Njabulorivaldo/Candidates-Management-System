# Generated by Django 4.2.8 on 2023-12-14 03:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("email", models.CharField(max_length=150, unique=True)),
                ("fullname", models.CharField(max_length=150)),
                ("password", models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name="Candidate",
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
                ("name", models.CharField(max_length=150)),
                ("contact", models.CharField(max_length=150)),
                ("email_add", models.EmailField(max_length=254, unique=True)),
                ("notes", models.TextField(max_length=1500)),
                ("date_added", models.DateTimeField(auto_now_add=True)),
                ("resume", models.FileField(upload_to="documents/")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="App.user"
                    ),
                ),
            ],
        ),
    ]