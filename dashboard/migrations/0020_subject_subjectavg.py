# Generated by Django 4.0.3 on 2023-04-20 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0019_grade_avg'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='subjectavg',
            field=models.FloatField(default=0, null=True),
        ),
    ]
