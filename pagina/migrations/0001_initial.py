# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=60)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_fin', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Asignacion',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nombre_asignacion', models.CharField(max_length=60)),
                ('fondos', models.CharField(max_length=50)),
                ('recursos_humano', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Dificultad',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=60)),
                ('direccion', models.CharField(max_length=120)),
                ('telefono', models.CharField(max_length=15)),
                ('correo', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Prioridad',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=60)),
                ('actividades', models.ManyToManyField(to='pagina.Actividad')),
            ],
        ),
        migrations.AddField(
            model_name='asignacion',
            name='empresa',
            field=models.ForeignKey(to='pagina.Empresa'),
        ),
        migrations.AddField(
            model_name='asignacion',
            name='proyectos',
            field=models.ManyToManyField(to='pagina.Proyecto'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='dificultad',
            field=models.ForeignKey(to='pagina.Dificultad'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='prioridad',
            field=models.ForeignKey(to='pagina.Prioridad'),
        ),
    ]
