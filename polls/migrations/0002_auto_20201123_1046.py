# Generated by Django 3.1.3 on 2020-11-23 01:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='querstion_text',
            new_name='question_text',
        ),
    ]
