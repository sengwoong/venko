# Generated by Django 3.2 on 2023-11-06 05:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tube', '0015_auto_20231102_2253'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('post_contents', models.TextField()),
                ('category', models.CharField(db_index=True, default='bug', max_length=50)),
                ('tags', models.CharField(blank=True, max_length=255)),
                ('title', models.CharField(db_index=True, max_length=100)),
                ('view_count', models.PositiveIntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clear_posts_written', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('bug', '버그'), ('quest', '퀘스트'), ('help', '도움'), ('rescue', '구조')], default='bug', max_length=50),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag_name',
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name='ClearPost',
        ),
    ]
