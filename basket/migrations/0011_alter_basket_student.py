# Generated by Django 4.0.4 on 2022-04-19 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_alter_student_parent'),
        ('basket', '0010_alter_basket_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='student',
            field=models.ManyToManyField(blank=True, related_name='baskets', to='students.student'),
        ),
    ]
