# Generated by Django 4.0.4 on 2022-06-07 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_teacher', '0010_alter_receipt_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receipt',
            name='ingredients',
        ),
    ]
