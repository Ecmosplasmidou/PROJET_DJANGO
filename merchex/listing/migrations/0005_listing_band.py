# Generated by Django 5.1.1 on 2024-10-02 08:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("listing", "0004_listing_description_listing_sold_listing_type_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="listing",
            name="band",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="listing.band",
            ),
        ),
    ]
