# Generated by Django 3.2.10 on 2022-06-03 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_comments',
            field=models.TextField(),
        ),
    ]