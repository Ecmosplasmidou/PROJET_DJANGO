# Generated by Django 5.1.1 on 2024-10-02 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("listing", "0008_listing_mandro"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="listing",
            name="mandro",
        ),
    ]
