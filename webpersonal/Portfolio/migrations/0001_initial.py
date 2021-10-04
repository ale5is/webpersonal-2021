# Generated by Django 3.2.5 on 2021-10-04 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Título')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('img', models.ImageField(upload_to='project', verbose_name='Imagen')),
                ('link', models.URLField(blank=True, null=True, verbose_name='Enlace')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
            ],
            options={
                'verbose_name': 'Projecto',
                'verbose_name_plural': 'Projectos',
                'ordering': ['created'],
            },
        ),
    ]
