# Generated by Django 4.2 on 2024-01-31 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_account_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='review',
            field=models.TextField(default='', max_length=100),
        ),
    ]
