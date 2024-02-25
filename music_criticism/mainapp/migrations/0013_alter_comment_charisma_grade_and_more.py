# Generated by Django 5.0.1 on 2024-02-25 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_comment_charisma_grade_comment_rate_grade_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='charisma_grade',
            field=models.PositiveSmallIntegerField(blank=True, choices=[], default=5),
        ),
        migrations.AlterField(
            model_name='comment',
            name='rate_grade',
            field=models.PositiveSmallIntegerField(blank=True, choices=[], default=5),
        ),
        migrations.AlterField(
            model_name='comment',
            name='realizationstyle_grade',
            field=models.PositiveSmallIntegerField(blank=True, choices=[], default=5),
        ),
        migrations.AlterField(
            model_name='comment',
            name='structurerhythm',
            field=models.PositiveSmallIntegerField(blank=True, choices=[], default=5),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text_grade',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=5),
        ),
    ]
