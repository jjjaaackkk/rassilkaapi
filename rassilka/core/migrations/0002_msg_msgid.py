# Generated by Django 4.2.3 on 2023-07-07 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='msg',
            name='msgId',
            field=models.PositiveBigIntegerField(default=0, unique=True),
        ),
    ]