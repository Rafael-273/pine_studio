# Generated by Django 5.1.3 on 2024-12-12 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pine', '0006_remove_downloademail_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='downloademail',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='E-mail'),
        ),
    ]