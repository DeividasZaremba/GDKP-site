# Generated by Django 4.1.6 on 2023-03-27 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wowchar',
            name='char_class',
        ),
        migrations.AddField(
            model_name='wowchar',
            name='char_class',
            field=models.OneToOneField(help_text='Select class for this char', null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.wowclass'),
        ),
    ]