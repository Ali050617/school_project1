# Generated by Django 5.1.4 on 2024-12-06 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=100)),
                ('location', models.TextField()),
                ('date', models.DateField()),
                ('sport_type', models.CharField(max_length=100)),
            ],
        ),
    ]