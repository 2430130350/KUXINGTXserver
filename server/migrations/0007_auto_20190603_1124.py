# Generated by Django 2.2.1 on 2019-06-03 03:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0006_auto_20190603_1119'),
    ]

    operations = [
        migrations.RenameField(
            model_name='relation',
            old_name='discription',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='relation',
            old_name='fconfifm',
            new_name='fconfirm',
        ),
    ]
