# Generated by Django 4.2.7 on 2023-11-26 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='seat',
        ),
        migrations.AddField(
            model_name='ticket',
            name='seat',
            field=models.ManyToManyField(to='movies.seat'),
        ),
    ]
