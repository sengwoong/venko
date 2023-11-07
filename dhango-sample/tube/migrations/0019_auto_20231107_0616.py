# Generated by Django 3.2 on 2023-11-06 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tube', '0018_alter_posthistory_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='finecheck',
        ),
        migrations.AddField(
            model_name='comment',
            name='back_idx',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='front_idx',
            field=models.TextField(blank=True, null=True),
        ),
    ]