# Generated by Django 4.0.3 on 2023-06-24 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacherui', '0003_teacher_school'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='num_classes',
            field=models.IntegerField(default=0),
        ),
    ]
