# Generated by Django 4.2.7 on 2023-12-11 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payed',
            field=models.BooleanField(default=False),
        ),
    ]
