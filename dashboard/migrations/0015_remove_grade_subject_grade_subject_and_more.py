# Generated by Django 4.0.3 on 2023-01-06 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0014_remove_grade_subject_grade_subject_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grade',
            name='subject',
        ),
        migrations.AddField(
            model_name='grade',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.subject'),
        ),
        migrations.RemoveField(
            model_name='subject',
            name='profile',
        ),
        migrations.AddField(
            model_name='subject',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.profile'),
        ),
    ]
