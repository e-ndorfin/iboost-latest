# Generated by Django 4.0.3 on 2023-01-21 10:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0017_grade_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
