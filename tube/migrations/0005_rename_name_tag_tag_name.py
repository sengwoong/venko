# Generated by Django 3.2 on 2023-11-02 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tube', '0004_auto_20231102_1441'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='name',
            new_name='tag_name',
        ),
    ]