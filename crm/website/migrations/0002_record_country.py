# Generated by Django 5.0.7 on 2024-07-20 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='country',
            field=models.CharField(default='Default Country', max_length=100),
        ),
    ]
