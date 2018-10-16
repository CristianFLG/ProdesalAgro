# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-16 00:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agricultores',
            fields=[
                ('id_agricultor', models.IntegerField(primary_key=True, serialize=False)),
                ('rut', models.CharField(blank=True, db_column='Rut', max_length=10, null=True)),
                ('cv', models.CharField(blank=True, db_column='Cv', max_length=2, null=True)),
                ('nombres', models.CharField(blank=True, db_column='Nombres', max_length=50, null=True)),
                ('apellidos', models.CharField(blank=True, db_column='Apellidos', max_length=100, null=True)),
                ('sexo', models.CharField(blank=True, db_column='Sexo', max_length=2, null=True)),
                ('proyectos', models.CharField(blank=True, db_column='Proyectos', max_length=100, null=True)),
                ('edad', models.TextField(blank=True, db_column='Edad', max_length=2, null=True)),
                ('ingresos', models.CharField(blank=True, db_column='Ingresos', max_length=100, null=True)),
                ('superficie', models.CharField(blank=True, db_column='Superficie', max_length=3, null=True)),
            ],
            options={
                'db_table': 'Agricultores',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Aguasgrises',
            fields=[
                ('id_aguasgrises', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_aguasgrises', models.CharField(blank=True, db_column='Nombre_aguasgrises', max_length=3, null=True)),
            ],
            options={
                'db_table': 'AguasGrises',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Alcantarillado',
            fields=[
                ('id_alcantarillado', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_alcantarillado', models.CharField(blank=True, db_column='Nombre_alcantarillado', max_length=20, null=True)),
            ],
            options={
                'db_table': 'Alcantarillado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Apr',
            fields=[
                ('id_apr', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_apr', models.CharField(blank=True, db_column='Nombre_apr', max_length=3, null=True)),
            ],
            options={
                'db_table': 'Apr',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Asesoria',
            fields=[
                ('id_asesoria', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_asesoria', models.CharField(blank=True, db_column='Nombre_asesoria', max_length=20, null=True)),
            ],
            options={
                'db_table': 'Asesoria',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Aves',
            fields=[
                ('id_aves', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_aves', models.CharField(blank=True, db_column='Nombre_aves', max_length=20, null=True)),
                ('numero_gallinas', models.CharField(blank=True, db_column='Numero_gallinas', max_length=3, null=True)),
                ('numero_pollos', models.CharField(blank=True, db_column='Numero_pollos', max_length=3, null=True)),
                ('numero_huevosdialargo', models.CharField(blank=True, db_column='Numero_Huevosdialargo', max_length=3, null=True)),
                ('numero_huevosdiacorto', models.CharField(blank=True, db_column='Numero_Huevosdiacorto', max_length=3, null=True)),
                ('preciobandeja', models.CharField(blank=True, db_column='Preciobandeja', max_length=10, null=True)),
                ('tipo_venta', models.CharField(blank=True, db_column='Tipo_venta', max_length=20, null=True)),
            ],
            options={
                'db_table': 'Aves',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Bobinos',
            fields=[
                ('id_bobinos', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad_bobinos', models.CharField(blank=True, db_column='Cantidad_bobinos', max_length=5, null=True)),
                ('cantidad_diio', models.CharField(blank=True, db_column='Cantidad_diio', max_length=5, null=True)),
                ('sag', models.CharField(blank=True, db_column='Sag', max_length=3, null=True)),
                ('fardosalanio', models.CharField(blank=True, db_column='Fardosalanio', max_length=5, null=True)),
                ('lugar', models.CharField(blank=True, db_column='Lugar', max_length=50, null=True)),
                ('praderas', models.CharField(blank=True, db_column='Praderas', max_length=100, null=True)),
                ('ventas', models.CharField(blank=True, db_column='Ventas', max_length=20, null=True)),
            ],
            options={
                'db_table': 'Bobinos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Capitalcultural',
            fields=[
                ('id_capitalcultural', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_capitalcultural', models.CharField(blank=True, db_column='Nombre_Capitalcultural', max_length=20, null=True)),
            ],
            options={
                'db_table': 'Capitalcultural',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Colmenas',
            fields=[
                ('id_colmena', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.CharField(blank=True, db_column='Cantidad', max_length=4, null=True)),
                ('kg_colmena', models.CharField(blank=True, db_column='Kg_colmena', max_length=4, null=True)),
                ('perdidas', models.CharField(blank=True, db_column='Perdidas', max_length=4, null=True)),
                ('tipo_venta', models.CharField(blank=True, db_column='Tipo_Venta', max_length=20, null=True)),
            ],
            options={
                'db_table': 'Colmenas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Erosion',
            fields=[
                ('id_erocion', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_erocion', models.CharField(blank=True, db_column='Nombre_erocion', max_length=3, null=True)),
            ],
            options={
                'db_table': 'Erosion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Escolaridad',
            fields=[
                ('id_escolaridad', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_escolaridad', models.CharField(blank=True, db_column='Nombre_escolaridad', max_length=3, null=True)),
            ],
            options={
                'db_table': 'Escolaridad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Estanque',
            fields=[
                ('id_estanque', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_estanque', models.CharField(blank=True, db_column='Nombre_estanque', max_length=3, null=True)),
                ('tipo_concreto', models.CharField(blank=True, db_column='Tipo_concreto', max_length=20, null=True)),
            ],
            options={
                'db_table': 'Estanque',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Habita',
            fields=[
                ('id_habita', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_habita', models.CharField(blank=True, db_column='Nombre_habita', max_length=5, null=True)),
            ],
            options={
                'db_table': 'Habita',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Huertofamiliar',
            fields=[
                ('id_guardasemillas', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_huertofamiliar', models.CharField(blank=True, db_column='Nombre_huertofamiliar', max_length=3, null=True)),
                ('nombre_guardarsemillas', models.CharField(blank=True, db_column='Nombre_guardarsemillas', max_length=3, null=True)),
            ],
            options={
                'db_table': 'Huertofamiliar',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Inscrita',
            fields=[
                ('id_inscrita', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_inscrita', models.CharField(blank=True, db_column='Nombre_inscrita', max_length=3, null=True)),
            ],
            options={
                'db_table': 'Inscrita',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Nativo',
            fields=[
                ('id_nativo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_nativo', models.CharField(blank=True, db_column='Nombre_nativo', max_length=3, null=True)),
            ],
            options={
                'db_table': 'Nativo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Necesidad',
            fields=[
                ('id_necesidad', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_necesidad', models.CharField(blank=True, db_column='Tipo_necesidad', max_length=100, null=True)),
                ('tipo_amenaza', models.CharField(blank=True, db_column='Tipo_amenaza', max_length=200, null=True)),
            ],
            options={
                'db_table': 'Necesidad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rubro',
            fields=[
                ('id_rubro', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_rubro', models.CharField(blank=True, db_column='Nombre_rubro', max_length=50, null=True)),
                ('tipo', models.CharField(blank=True, db_column='Tipo', max_length=100, null=True)),
            ],
            options={
                'db_table': 'Rubro',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sag',
            fields=[
                ('id_sag', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_sag', models.CharField(blank=True, db_column='Nombre_sag', max_length=5, null=True)),
            ],
            options={
                'db_table': 'Sag',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id_sector', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_sector', models.CharField(blank=True, db_column='Nombre_sector', max_length=50, null=True)),
            ],
            options={
                'db_table': 'Sector',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Segmento',
            fields=[
                ('id_segmento', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_segmento', models.CharField(blank=True, db_column='Nombre_segmento', max_length=50, null=True)),
            ],
            options={
                'db_table': 'Segmento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Superficial',
            fields=[
                ('id_superficial', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_superficial', models.CharField(blank=True, db_column='Nombre_superficial', max_length=3, null=True)),
            ],
            options={
                'db_table': 'Superficial',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tenencia',
            fields=[
                ('id_tenencia', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_tenencia', models.CharField(blank=True, db_column='Nombre_tenencia', max_length=50, null=True)),
            ],
            options={
                'db_table': 'Tenencia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Turismo',
            fields=[
                ('id_turismo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_turismo', models.CharField(blank=True, db_column='Nombre_turismo', max_length=3, null=True)),
                ('tipo_turismo', models.CharField(blank=True, db_column='Tipo_turismo', max_length=20, null=True)),
            ],
            options={
                'db_table': 'Turismo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Vertiente',
            fields=[
                ('id_vertiente', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_vertiente', models.CharField(blank=True, db_column='Nombre_vertiente', max_length=3, null=True)),
            ],
            options={
                'db_table': 'Vertiente',
                'managed': False,
            },
        ),
    ]