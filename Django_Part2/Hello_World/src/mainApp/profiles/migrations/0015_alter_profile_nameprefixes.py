# Generated by Django 3.2.5 on 2021-07-24 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0014_alter_profile_nameprefixes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='namePrefixes',
            field=models.CharField(choices=[('Mr.', 'Mr.'), ('Ms.', 'Ms.'), ('Mrs.', 'Mrs.')], default='', max_length=4),
        ),
    ]
