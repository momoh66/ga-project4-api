# Generated by Django 4.0.4 on 2022-04-17 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0002_rename_recipient_message_recipient_parent_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='recipient_parent_id',
            new_name='recipient_parent',
        ),
    ]