# Generated by Django 5.0.3 on 2024-03-07 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppMusicy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='songs',
            field=models.CharField(default='Varias', max_length=60),
            preserve_default=False,
        ),
    ]
