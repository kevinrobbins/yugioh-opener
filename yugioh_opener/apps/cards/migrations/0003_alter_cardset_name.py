# Generated by Django 3.2.6 on 2021-08-23 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_rename_full_name_cardset_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardset',
            name='name',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
