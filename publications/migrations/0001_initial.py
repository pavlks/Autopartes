# Generated by Django 3.0.5 on 2020-05-05 22:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publication_title', models.CharField(max_length=200, verbose_name='Título de anuncio')),
                ('publication_author', models.CharField(max_length=60, verbose_name='Su nombre')),
                ('publication_description', models.TextField(verbose_name='Descripción')),
                ('publication_date', models.DateTimeField(verbose_name='Fecha de publicación')),
                ('publication_image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Imagen')),
                ('publication_objective', models.CharField(max_length=50, verbose_name='Busca u ofrece?')),
            ],
            options={
                'verbose_name': 'Publication',
                'verbose_name_plural': 'Publications',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_author', models.CharField(max_length=60, verbose_name='Su nombre')),
                ('comment_text', models.CharField(max_length=200, verbose_name='Comentario')),
                ('publication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publications.Publication')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
    ]
