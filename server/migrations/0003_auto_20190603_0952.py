# Generated by Django 2.2.1 on 2019-06-03 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_relation'),
    ]

    operations = [
        migrations.AddField(
            model_name='relation',
            name='fconfifm',
            field=models.IntegerField(default=0, max_length=2, null=0, verbose_name='f确认'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='relation',
            name='mconfirm',
            field=models.IntegerField(default=0, max_length=2, null=0, verbose_name='m确认'),
            preserve_default=False,
        ),
    ]
