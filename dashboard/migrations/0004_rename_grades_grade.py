# Generated by Django 4.0.4 on 2022-09-21 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_grades_remove_user_grade_remove_subject_score_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Grades',
            new_name='Grade',
        ),
    ]
