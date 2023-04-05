# Generated by Django 4.1.6 on 2023-04-05 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0021_remove_wowplayer_wow_char_wowplayer_char_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wowplayer',
            name='char_id',
        ),
        migrations.AddField(
            model_name='wowplayer',
            name='wow_char',
            field=models.ManyToManyField(blank=True, help_text='Players characters', to='library.wowchar'),
        ),
    ]
