# Generated by Django 4.2.9 on 2024-05-23 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
