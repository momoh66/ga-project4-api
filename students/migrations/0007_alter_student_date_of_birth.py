# Generated by Django 4.0.4 on 2022-04-21 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_student_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(max_length=6, null=True),
        ),
    ]
