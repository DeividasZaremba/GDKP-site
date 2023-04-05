# Generated by Django 4.1.6 on 2023-04-03 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0015_alter_wowchar_wow_player_alter_wowplayer_wow_char'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wowchar',
            name='char_class',
        ),
        migrations.AddField(
            model_name='wowchar',
            name='char_class',
            field=models.ManyToManyField(help_text='Select class for this char.', to='library.wowclass'),
        ),
    ]
