# Generated by Django 2.2.1 on 2019-06-03 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0007_auto_20190603_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='date',
            field=models.DateTimeField(verbose_name='日期'),
        ),
        migrations.AlterField(
            model_name='trends',
            name='date',
            field=models.DateTimeField(verbose_name='日期'),
        ),
    ]