# Generated by Django 5.1.3 on 2024-12-04 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pine', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(db_index=True, editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.AddField(
            model_name='pack',
            name='cover',
            field=models.ImageField(default='', upload_to='packs_covers/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pack',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, unique=True),
        ),
        migrations.AddField(
            model_name='pack',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='packs', to='pine.tag'),
        ),
    ]
