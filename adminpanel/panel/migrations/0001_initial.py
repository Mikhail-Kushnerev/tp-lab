# Generated by Django 4.1 on 2022-08-19 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('user_id', models.IntegerField()),
                ('domen', models.CharField(max_length=200)),
            ],
        ),
    ]
