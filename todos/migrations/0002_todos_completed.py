# Generated by Django 3.2.5 on 2021-07-21 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todos',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
