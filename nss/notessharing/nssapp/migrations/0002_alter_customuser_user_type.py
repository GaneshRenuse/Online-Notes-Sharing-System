# Generated by Django 5.0.6 on 2024-05-20 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nssapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(2, 'nsuser'), (1, 'admin')], default=1, max_length=50),
        ),
    ]
