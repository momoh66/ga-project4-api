# Generated by Django 4.0.4 on 2022-04-17 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_student_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='sex',
            field=models.CharField(default=1, max_length=6),
            preserve_default=False,
        ),
    ]
