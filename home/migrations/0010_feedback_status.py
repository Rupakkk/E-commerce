# Generated by Django 3.1.7 on 2021-03-31 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='status',
            field=models.CharField(choices=[('active', 'active'), ('passive', 'passive')], default=None, max_length=200),
        ),
    ]
