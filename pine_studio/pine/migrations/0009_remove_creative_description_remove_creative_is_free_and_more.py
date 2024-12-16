# Generated by Django 5.1.3 on 2024-12-13 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pine', '0008_contactmessage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creative',
            name='description',
        ),
        migrations.RemoveField(
            model_name='creative',
            name='is_free',
        ),
        migrations.AddField(
            model_name='creative',
            name='dimensions',
            field=models.CharField(choices=[('1080x1350', '1080 x 1350'), ('1080X1920', '1080 x 1920'), ('1080x1080', '1080 x 1080')], default='1080x1350', max_length=9),
        ),
    ]