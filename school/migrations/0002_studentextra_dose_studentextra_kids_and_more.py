# Generated by Django 4.0.6 on 2022-07-26 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentextra',
            name='dose',
            field=models.CharField(choices=[('first', 'first'), ('second', 'second')], default='first', max_length=10),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='kids',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='vaccdate',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='studentextra',
            name='vacctype',
            field=models.CharField(choices=[('covishield', 'covishield'), ('covaxin', 'covaxin'), ('sputnik', 'sputnik')], default='covishield', max_length=10),
        ),
        migrations.AlterField(
            model_name='studentextra',
            name='pregnancy',
            field=models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='no', max_length=10),
        ),
    ]