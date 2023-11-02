# Generated by Django 3.2 on 2023-11-02 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tube', '0003_auto_20231102_1415'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_images',
        ),
        migrations.AddField(
            model_name='postcontent',
            name='file_upload',
            field=models.FileField(blank=True, upload_to='tube/files/%Y/%m/%d/'),
        ),
        migrations.DeleteModel(
            name='PostImage',
        ),
    ]
