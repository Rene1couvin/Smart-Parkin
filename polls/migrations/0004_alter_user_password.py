# Generated by Django 5.0.3 on 2024-05-31 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_alter_user_idnumber_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='', max_length=100),
        ),
    ]
