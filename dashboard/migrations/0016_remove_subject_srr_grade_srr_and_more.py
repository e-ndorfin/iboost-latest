# Generated by Django 4.0.3 on 2023-01-21 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0015_remove_grade_subject_grade_subject_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='srr',
        ),
        migrations.AddField(
            model_name='grade',
            name='srr',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='subjectname',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
