# Generated by Django 4.0.2 on 2022-02-14 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minimum_prices', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mod',
            name='servers',
            field=models.ManyToManyField(related_name='mods', to='minimum_prices.Server', verbose_name='Сервера на которых установлен'),
        ),
    ]
