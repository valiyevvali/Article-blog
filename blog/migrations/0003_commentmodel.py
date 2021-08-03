# Generated by Django 3.2.6 on 2021-08-03 08:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_auto_20210803_0021'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yorumlar', to='blog.articlemodel')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yorum', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'Comments',
                'db_table': 'Comment',
            },
        ),
    ]
