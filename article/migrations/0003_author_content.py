# Generated by Django 5.0.1 on 2024-01-22 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_alter_article_content_alter_comment_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
