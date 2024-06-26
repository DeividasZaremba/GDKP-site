# Generated by Django 4.1.6 on 2023-03-29 12:52

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_remove_wowchar_char_class_wowchar_char_class'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wowchar',
            options={'ordering': ['char_title']},
        ),
        migrations.AlterModelOptions(
            name='wowclass',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='wowspec',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='charinstance',
            name='due_back',
            field=models.DateField(blank=True, null=True, verbose_name='Will be available.'),
        ),
        migrations.AlterField(
            model_name='charinstance',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unique character ID.', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='wowchar',
            name='char_class',
            field=models.OneToOneField(help_text='Select class for this char.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.wowclass'),
        ),
        migrations.RemoveField(
            model_name='wowchar',
            name='char_spec',
        ),
        migrations.AlterField(
            model_name='wowchar',
            name='logs_link',
            field=models.TextField(help_text='Link to Warcraftlogs.', max_length=200, verbose_name='Warcraft logs link'),
        ),
        migrations.AlterField(
            model_name='wowclass',
            name='name',
            field=models.CharField(help_text='Character class.', max_length=20, verbose_name='Class'),
        ),
        migrations.AlterField(
            model_name='wowspec',
            name='name',
            field=models.CharField(help_text='Character specialization.', max_length=20, verbose_name='Spec'),
        ),
        migrations.AddField(
            model_name='wowchar',
            name='char_spec',
            field=models.OneToOneField(help_text='Select spec for this char.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.wowspec'),
        ),
    ]
