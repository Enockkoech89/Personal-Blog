# Generated by Django 3.0.5 on 2020-05-23 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_auto_20200515_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('T', 'Technology'), ('E', 'Socio/Econ')], max_length=1),
        ),
    ]