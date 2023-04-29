# Generated by Django 4.1.6 on 2023-04-28 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0032_alter_wowplayer_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wowplayer',
            name='description',
            field=models.TextField(default='', max_length=2000, verbose_name='About you'),
        ),
        migrations.AlterField(
            model_name='wowplayer',
            name='discord_tag',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Discord tag'),
        ),
    ]