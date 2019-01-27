# Generated by Django 2.1.5 on 2019-01-22 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=22)),
                ('email', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=15)),
                ('date', models.CharField(max_length=30)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=50)),
                ('content', models.TextField()),
                ('date', models.CharField(max_length=40)),
                ('slug', models.CharField(max_length=40)),
                ('img_file', models.CharField(max_length=40)),
                ('sub_heading', models.TextField()),
            ],
        ),
    ]