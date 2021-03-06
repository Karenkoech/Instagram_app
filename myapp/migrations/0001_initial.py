# Generated by Django 3.2.10 on 2022-06-03 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_bio', models.TextField()),
                ('profile_image', models.ImageField(upload_to='')),
                ('profile_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('image_name', models.CharField(max_length=50)),
                ('image_caption', models.TextField()),
                ('image_date', models.DateTimeField(auto_now_add=True)),
                ('image_likes', models.IntegerField(default=0)),
                ('image_comments', models.IntegerField(default=0)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.profile')),
            ],
        ),
    ]
