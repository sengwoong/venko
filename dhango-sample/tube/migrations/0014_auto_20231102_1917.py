# Generated by Django 3.2 on 2023-11-02 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tube', '0013_auto_20231102_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='posts', to='tube.Tag'),
        ),
        migrations.AlterField(
            model_name='postcontent',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postcontents', to='tube.post'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posttags', to='tube.post'),
        ),
    ]
