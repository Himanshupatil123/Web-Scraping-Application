# Generated by Django 4.2.9 on 2024-05-21 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email_id', models.CharField(max_length=100)),
                ('product_name', models.CharField(max_length=400)),
                ('alert_price', models.IntegerField()),
            ],
        ),
    ]
