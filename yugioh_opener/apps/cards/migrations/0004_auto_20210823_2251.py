# Generated by Django 3.2.6 on 2021-08-23 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0003_alter_cardset_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardattribute',
            name='name',
            field=models.CharField(max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='cardtype',
            name='name',
            field=models.CharField(max_length=32, unique=True),
        ),
    ]