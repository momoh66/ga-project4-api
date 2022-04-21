# Generated by Django 4.0.4 on 2022-04-20 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0003_remove_teacher_student_teacher_student'),
        ('messaging', '0003_rename_recipient_parent_id_message_recipient_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='messages', to='teachers.teacher'),
        ),
    ]