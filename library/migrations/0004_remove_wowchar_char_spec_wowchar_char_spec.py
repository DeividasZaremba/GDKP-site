# Generated by Django 4.1.6 on 2023-03-29 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_alter_wowchar_options_alter_wowclass_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wowchar',
            name='char_spec',
        ),
        migrations.AddField(
            model_name='wowchar',
            name='char_spec',
            field=models.ManyToManyField(help_text='Select spec for this char.', to='library.wowspec'),
        ),
    ]
