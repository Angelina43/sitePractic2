# Generated by Django 3.2.16 on 2022-11-22 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advuser',
            name='send_messages',
        ),
        migrations.AddField(
            model_name='advuser',
            name='apply_personal_data',
            field=models.BooleanField(default=False, verbose_name='Согласие на обработку персональных данных'),
        ),
        migrations.AddField(
            model_name='advuser',
            name='middle_name',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]
