# Generated by Django 3.2 on 2023-11-02 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tube', '0007_auto_20231102_1650'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postcontent',
            old_name='post_id',
            new_name='post',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='post_id',
            new_name='post',
        ),
    ]
