# Generated by Django 4.1.2 on 2022-10-19 08:06

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
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('qualification', models.CharField(max_length=255)),
                ('mobile_no', models.CharField(max_length=255)),
                ('skills', models.TextField(max_length=250)),
            ],
        ),
    ]