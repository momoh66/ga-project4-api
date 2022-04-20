# Generated by Django 4.0.4 on 2022-04-17 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_student_paid'),
        ('basket', '0004_alter_basket_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='baskets', to='students.student'),
        ),
    ]