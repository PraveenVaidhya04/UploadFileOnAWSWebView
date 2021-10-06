# Generated by Django 3.2.7 on 2021-10-04 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_posts', '0002_posts_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='url',
            field=models.CharField(blank=True, db_column='url', max_length=100, null=True, verbose_name='Post Url'),
        ),
    ]
