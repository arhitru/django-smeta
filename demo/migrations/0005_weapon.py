# Generated by Django 4.2.11 on 2024-06-02 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0004_remove_order_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('power', models.IntegerField()),
                ('rarity', models.CharField(max_length=50)),
                ('value', models.IntegerField()),
            ],
        ),
    ]
