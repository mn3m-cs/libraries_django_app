# Generated by Django 3.1 on 2021-03-10 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_auto_20210305_0817'),
    ]

    operations = [
        migrations.AddField(
            model_name='librarybooks',
            name='price',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]
