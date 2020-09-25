# Generated by Django 3.1.1 on 2020-09-24 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('surname', models.CharField(max_length=60)),
                ('gender', models.CharField(choices=[('MALE', 'male'), ('FEMALE', 'female')], max_length=6)),
                ('biography', models.TextField()),
                ('awards', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('icon', models.ImageField(upload_to='')),
                ('url', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Actor',
                'verbose_name_plural': 'Actors',
            },
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('surname', models.CharField(max_length=60)),
                ('gender', models.CharField(choices=[('MALE', 'male'), ('FEMALE', 'female')], max_length=6)),
                ('biography', models.TextField()),
                ('awards', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('icon', models.ImageField(upload_to='')),
                ('url', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Producer',
                'verbose_name_plural': 'Producers',
            },
        ),
    ]
