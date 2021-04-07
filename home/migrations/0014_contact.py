# Generated by Django 3.1.7 on 2021-04-04 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_item_specification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('subject', models.TextField(blank=True)),
                ('message', models.TextField()),
            ],
        ),
    ]