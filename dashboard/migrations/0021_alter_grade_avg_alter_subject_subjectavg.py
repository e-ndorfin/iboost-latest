# Generated by Django 4.0.3 on 2023-04-20 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0020_subject_subjectavg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='avg',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2, null=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='subjectavg',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2, null=True),
        ),
    ]
