# Generated by Django 2.2 on 2019-05-08 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='editor',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]