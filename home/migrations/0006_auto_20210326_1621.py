# Generated by Django 3.1.7 on 2021-03-26 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210326_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='status',
            field=models.CharField(choices=[('activeee', 'active'), ('passive', 'passive')], max_length=200),
        ),
        migrations.AlterField(
            model_name='brand',
            name='status',
            field=models.CharField(choices=[('activeee', 'active'), ('passive', 'passive')], max_length=200),
        ),
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.CharField(choices=[('activeee', 'active'), ('passive', 'passive')], max_length=200),
        ),
        migrations.AlterField(
            model_name='item',
            name='status',
            field=models.CharField(choices=[('activeee', 'active'), ('passive', 'passive')], max_length=200),
        ),
        migrations.AlterField(
            model_name='slider',
            name='status',
            field=models.CharField(choices=[('activeee', 'active'), ('passive', 'passive')], max_length=200),
        ),
    ]
