# Generated by Django 3.2.5 on 2021-07-25 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0030_alter_profile_nameprefixes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='namePrefixes',
            field=models.CharField(choices=[('Ms.', 'Ms.'), ('Mrs.', 'Mrs.'), ('Mr.', 'Mr.')], default='', max_length=4),
        ),
    ]
