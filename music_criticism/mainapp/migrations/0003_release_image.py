# Generated by Django 4.2.8 on 2023-12-17 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_rename_title_release_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='release',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/%Y/%m/%d/'),
        ),
    ]
