# Generated by Django 5.0.1 on 2024-01-10 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_alter_comment_pub_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='pub_date',
        ),
    ]