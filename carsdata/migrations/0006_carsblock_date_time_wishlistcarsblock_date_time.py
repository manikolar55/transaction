# Generated by Django 4.1.3 on 2022-12-20 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("carsdata", "0005_wishlistblock_wishlistcarsblock"),
    ]

    operations = [
        migrations.AddField(
            model_name="carsblock",
            name="date_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="wishlistcarsblock",
            name="date_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]