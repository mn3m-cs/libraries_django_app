# Generated by Django 3.1 on 2021-03-12 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0014_remove_book_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.CharField(default='en', max_length=50),
            preserve_default=False,
        ),
    ]
