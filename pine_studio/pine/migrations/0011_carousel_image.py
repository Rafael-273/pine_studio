# Generated by Django 5.1.3 on 2024-12-16 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pine', '0010_carousel_creative_carousels'),
    ]

    operations = [
        migrations.AddField(
            model_name='carousel',
            name='image',
            field=models.ImageField(default='', upload_to='creatives/carousel'),
            preserve_default=False,
        ),
    ]
