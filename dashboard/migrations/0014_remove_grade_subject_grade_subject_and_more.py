# Generated by Django 4.0.3 on 2023-01-06 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_remove_profile_subjects_remove_subject_grade_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grade',
            name='subject',
        ),
        migrations.AddField(
            model_name='grade',
            name='subject',
            field=models.ManyToManyField(to='dashboard.subject'),
        ),
        migrations.RemoveField(
            model_name='subject',
            name='profile',
        ),
        migrations.AddField(
            model_name='subject',
            name='profile',
            field=models.ManyToManyField(to='dashboard.profile'),
        ),
    ]
