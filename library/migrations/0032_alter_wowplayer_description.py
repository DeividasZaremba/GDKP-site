# Generated by Django 4.1.6 on 2023-04-28 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0031_wowplayer_discord_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wowplayer',
            name='description',
            field=models.TextField(default='', max_length=2000, null=True, verbose_name='About you'),
        ),
    ]
