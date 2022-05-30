# Generated by Django 2.2.16 on 2022-03-11 17:40

import django.db.models.expressions
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20220311_2150'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='review',
            constraint=models.CheckConstraint(check=models.Q(_negated=True, author=django.db.models.expressions.F('title')), name='Вы уже оставили отзыв'),
        ),
    ]
