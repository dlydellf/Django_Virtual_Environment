# Generated by Django 3.2.5 on 2021-07-25 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0026_alter_profile_nameprefixes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='namePrefixes',
            field=models.CharField(choices=[('Mr.', 'Mr.'), ('Mrs.', 'Mrs.'), ('Ms.', 'Ms.')], default='', max_length=4),
        ),
    ]
