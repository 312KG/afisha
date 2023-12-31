# Generated by Django 5.0 on 2023-12-26 07:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.IntegerField(choices=[(1, '* '), (2, '* * '), (3, '* * * '), (4, '* * * * '), (5, '* * * * * ')], default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='movie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='movie_app.movie'),
        ),
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movie_app.genre'),
        ),
        migrations.AddField(
            model_name='movie',
            name='tags',
            field=models.ManyToManyField(blank=True, to='movie_app.tag'),
        ),
    ]
