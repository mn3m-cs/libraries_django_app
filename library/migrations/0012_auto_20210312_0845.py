# Generated by Django 3.1 on 2021-03-12 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0011_librarybooks_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.SmallIntegerField(null=True),
        ),
    ]
