# Generated by Django 4.1.6 on 2023-03-30 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0012_rename_char_wowplayer_wow_char'),
    ]

    operations = [
        migrations.AddField(
            model_name='wowchar',
            name='gearscore',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='Gearscore'),
        ),
    ]
