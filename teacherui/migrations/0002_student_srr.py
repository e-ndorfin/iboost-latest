# Generated by Django 4.0.3 on 2023-06-24 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0026_srr_profile'),
        ('teacherui', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='srr',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.srr'),
        ),
    ]
