# Generated by Django 4.2.3 on 2023-07-07 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_msg_msgid'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='status',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
