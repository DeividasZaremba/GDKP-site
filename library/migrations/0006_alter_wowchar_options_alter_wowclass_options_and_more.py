# Generated by Django 4.1.6 on 2023-03-29 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_alter_wowchar_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wowchar',
            options={'ordering': ['char_title']},
        ),
        migrations.AlterModelOptions(
            name='wowclass',
            options={},
        ),
        migrations.AlterModelOptions(
            name='wowspec',
            options={'verbose_name': 'Spec', 'verbose_name_plural': 'Specs'},
        ),
    ]