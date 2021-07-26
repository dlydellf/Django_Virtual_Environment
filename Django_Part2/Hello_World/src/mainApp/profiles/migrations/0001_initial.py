# Generated by Django 3.2.5 on 2021-07-24 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namePrefixes', models.CharField(choices=[('Mr.', 'Mr.'), ('Mrs.', 'Mrs.'), ('Ms.', 'Ms.')], default='', max_length=4)),
                ('firstName', models.CharField(default='', max_length=60)),
                ('lastName', models.CharField(default='', max_length=60)),
                ('email', models.EmailField(default='', max_length=120)),
                ('userName', models.CharField(default='', max_length=60)),
            ],
        ),
    ]
