# Generated by Django 4.1 on 2023-05-19 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pose',
            name='image',
            field=models.ImageField(default='', upload_to='upload/'),
        ),
    ]
