# Generated by Django 4.2.9 on 2024-02-04 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bazaapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zakaz',
            name='data_oplati',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='zakaz',
            name='oplaceno',
            field=models.BooleanField(null=True),
        ),
    ]
