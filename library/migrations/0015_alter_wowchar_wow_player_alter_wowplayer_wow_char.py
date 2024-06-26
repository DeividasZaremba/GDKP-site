# Generated by Django 4.1.6 on 2023-03-30 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0014_remove_wowchar_gearscore_remove_wowchar_logs_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wowchar',
            name='wow_player',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.wowplayer'),
        ),
        migrations.AlterField(
            model_name='wowplayer',
            name='wow_char',
            field=models.ManyToManyField(blank=True, help_text='Players characters', to='library.wowchar'),
        ),
    ]
