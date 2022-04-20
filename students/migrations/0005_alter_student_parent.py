# Generated by Django 4.0.4 on 2022-04-19 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parents', '0002_remove_parent_students'),
        ('students', '0004_student_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='parent',
            field=models.ManyToManyField(related_name='students', to='parents.parent'),
        ),
    ]
