# Generated by Django 4.0.4 on 2022-05-24 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_article_pub_date_article_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='editor',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
