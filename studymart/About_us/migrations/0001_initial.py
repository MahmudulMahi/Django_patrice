# Generated by Django 4.1.1 on 2022-10-05 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tid', models.IntegerField()),
                ('tname', models.CharField(max_length=40)),
                ('temail', models.EmailField(max_length=30)),
            ],
        ),
    ]