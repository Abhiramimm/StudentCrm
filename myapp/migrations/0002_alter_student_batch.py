# Generated by Django 5.0.3 on 2024-04-04 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='batch',
            field=models.PositiveIntegerField(),
        ),
    ]
