# Generated by Django 5.1.1 on 2024-10-02 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("listing", "0006_listing_like_new_alter_listing_type"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="listing",
            name="like_new",
        ),
    ]
