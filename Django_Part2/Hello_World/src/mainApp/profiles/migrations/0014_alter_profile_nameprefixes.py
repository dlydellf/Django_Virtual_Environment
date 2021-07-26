# Generated by Django 3.2.5 on 2021-07-24 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0013_alter_profile_nameprefixes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='namePrefixes',
            field=models.CharField(choices=[('Mrs.', 'Mrs.'), ('Ms.', 'Ms.'), ('Mr.', 'Mr.')], default='', max_length=4),
        ),
    ]
