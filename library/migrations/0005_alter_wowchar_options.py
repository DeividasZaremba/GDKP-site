# Generated by Django 4.1.6 on 2023-03-29 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_remove_wowchar_char_spec_wowchar_char_spec'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wowchar',
            options={'ordering': ['char_title'], 'verbose_name': 'Char', 'verbose_name_plural': 'Chars'},
        ),
    ]
