# Generated by Django 4.0.3 on 2023-06-23 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0025_alter_srr_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='srr',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.profile'),
        ),
    ]
