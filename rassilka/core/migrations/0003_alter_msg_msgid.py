# Generated by Django 4.2.3 on 2023-07-07 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_msg_msgid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msg',
            name='msgId',
            field=models.PositiveBigIntegerField(unique=True),
        ),
    ]
