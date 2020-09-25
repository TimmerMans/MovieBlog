# Generated by Django 3.1.1 on 2020-09-24 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0004_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('url', models.SlugField(max_length=100, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genres', related_query_name='genres_query', to='MainApp.category')),
            ],
            options={
                'verbose_name': 'Genre',
                'verbose_name_plural': 'Genres',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('tagline', models.CharField(default='', max_length=100)),
                ('description', models.TextField()),
                ('budget', models.PositiveIntegerField()),
                ('world_premiere_date', models.DateField()),
                ('url', models.SlugField(max_length=120, unique=True)),
                ('draft', models.BooleanField(default=False)),
                ('actors', models.ManyToManyField(related_name='movies', related_query_name='movies_query', to='MainApp.Actor')),
                ('genres', models.ManyToManyField(related_name='movies', related_query_name='movies_query', to='MainApp.Genre')),
                ('producers', models.ManyToManyField(related_name='movies', related_query_name='movies_query', to='MainApp.Producer')),
            ],
            options={
                'verbose_name': 'Movie',
                'verbose_name_plural': 'Movies',
            },
        ),
    ]