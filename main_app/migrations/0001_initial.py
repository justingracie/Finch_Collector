# Generated by Django 4.0.4 on 2022-06-01 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.TextField(max_length=125)),
                ('year', models.CharField(max_length=20)),
                ('value', models.CharField(max_length=25)),
                ('quantity', models.CharField(max_length=25)),
            ],
            options={
                'ordering': ['type'],
            },
        ),
    ]