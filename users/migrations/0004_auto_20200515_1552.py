# Generated by Django 3.0.5 on 2020-05-15 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_biography'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='p_image',
            field=models.ImageField(default='profile.JPG', upload_to='profilepicsblog'),
        ),
    ]
