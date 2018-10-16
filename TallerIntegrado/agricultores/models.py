# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Agricultores(models.Model):
    id_agricultor = models.IntegerField(primary_key=True)  # Field name made lowercase.
    rut = models.CharField(db_column='Rut', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cv = models.CharField(db_column='Cv', max_length=2, blank=True, null=True)  # Field name made lowercase.
    nombres = models.CharField(db_column='Nombres', max_length=50, blank=True, null=True)  # Field name made lowercase.
    apellidos = models.CharField(db_column='Apellidos', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sexo = models.CharField(db_column='Sexo', max_length=2, blank=True, null=True)  # Field name made lowercase.
    proyectos = models.CharField(db_column='Proyectos', max_length=100, blank=True, null=True)  # Field name made lowercase.
    edad = models.CharField(db_column='Edad',max_length=2, blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ingresos = models.CharField(db_column='Ingresos', max_length=100, blank=True, null=True)  # Field name made lowercase.
    superficie = models.CharField(db_column='Superficie', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Agricultores'

    def __str__(self):
        return self.nombres


class Aguasgrises(models.Model):
    id_aguasgrises = models.AutoField(primary_key=True) # Field name made lowercase.
    nombre_aguasgrises = models.CharField(db_column='Nombre_aguasgrises', max_length=3, blank=True, null=True)  # Field name made lowercase.
    id_agricultor = models.ForeignKey(Agricultores, on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Aguasgrises'
def __str__(self):
        return self.nombre_aguasgrises

class Alcantarillado(models.Model):
    id_alcantarillado = models.AutoField(primary_key=True)  # Field name made lowercase.
    nombre_alcantarillado = models.CharField(db_column='Nombre_alcantarillado', max_length=20, blank=True, null=True)  # Field name made lowercase.
    id_agricultor = models.ForeignKey(Agricultores, on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Alcantarillado'

def __str__(self):
        return self.nombre_alcantarillado

class Apr(models.Model):
    id_apr = models.AutoField(primary_key=True)  # Field name made lowercase.
    nombre_apr = models.CharField(db_column='Nombre_apr', max_length=3, blank=True, null=True)  # Field name made lowercase.
    id_agricultor = models.ForeignKey(Agricultores, on_delete=models.CASCADE) 

    class Meta:
        managed = False
        db_table = 'Apr'

def __str__(self):
        return self.nombre_apr

class Asesoria(models.Model):
    id_asesoria = models.AutoField(primary_key=True)  # Field name made lowercase.
    nombre_asesoria = models.CharField(db_column='Nombre_asesoria', max_length=20, blank=True, null=True)  # Field name made lowercase.
    id_agricultor = models.ForeignKey(Agricultores, on_delete=models.CASCADE) 

    class Meta:
        managed = False
        db_table = 'Asesoria'

    def __str__(self):
        return self.nombre_asesoria


class Aves(models.Model):
    id_aves = models.AutoField(primary_key=True)  # Field name made lowercase.
    nombre_aves = models.CharField(db_column='Nombre_aves', max_length=20, blank=True, null=True)  # Field name made lowercase.
    numero_gallinas = models.CharField(db_column='Numero_gallinas', max_length=3, blank=True, null=True)  # Field name made lowercase.
    numero_pollos = models.CharField(db_column='Numero_pollos', max_length=3, blank=True, null=True)  # Field name made lowercase.
    numero_huevosdialargo = models.CharField(db_column='Numero_Huevosdialargo', max_length=3, blank=True, null=True)  # Field name made lowercase.
    numero_huevosdiacorto = models.CharField(db_column='Numero_Huevosdiacorto', max_length=3, blank=True, null=True)  # Field name made lowercase.
    preciobandeja = models.CharField(db_column='Preciobandeja', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tipo_venta = models.CharField(db_column='Tipo_venta', max_length=20, blank=True, null=True)  # Field name made lowercase.
    id_agricultor = models.ForeignKey(Agricultores, on_delete=models.CASCADE) 

    class Meta:
        managed = False
        db_table = 'Aves'

def __str__(self):
        return self.nombre_aves


class Bobinos(models.Model):
    id_bobinos = models.AutoField(primary_key=True)  # Field name made lowercase.
    cantidad_bobinos = models.CharField(db_column='Cantidad_bobinos', max_length=5, blank=True, null=True)  # Field name made lowercase.
    cantidad_diio = models.CharField(db_column='Cantidad_diio', max_length=5, blank=True, null=True)  # Field name made lowercase.
    sag = models.CharField(db_column='Sag', max_length=3, blank=True, null=True)  # Field name made lowercase.
    fardosalanio = models.CharField(db_column='Fardosalanio', max_length=5, blank=True, null=True)  # Field name made lowercase.
    lugar = models.CharField(db_column='Lugar', max_length=50, blank=True, null=True)  # Field name made lowercase.
    praderas = models.CharField(db_column='Praderas', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ventas = models.CharField(db_column='Ventas', max_length=20, blank=True, null=True)  # Field name made lowercase.
    id_agricultor = models.ForeignKey(Agricultores, on_delete=models.CASCADE) 

    class Meta:
        managed = False
        db_table = 'Bobinos'

def __str__(self):
        return self.cantidad_bobinos

class Capitalcultural(models.Model):
    id_capitalcultural = models.AutoField(primary_key=True)  # Field name made lowercase.
    nombre_capitalcultural = models.CharField(db_column='Nombre_Capitalcultural', max_length=20, blank=True, null=True)  # Field name made lowercase.
    id_agricultor = models.ForeignKey(Agricultores, on_delete=models.CASCADE) 

    class Meta:
        managed = False
        db_table = 'Capitalcultural'

def __str__(self):
        return self.nombre_capitalcultural

class Colmenas(models.Model):
    id_colmena = models.AutoField(primary_key=True)  # Field name made lowercase.
    cantidad = models.CharField(db_column='Cantidad', max_length=4, blank=True, null=True)  # Field name made lowercase.
    kg_colmena = models.CharField(db_column='Kg_colmena', max_length=4, blank=True, null=True)  # Field name made lowercase.
    perdidas = models.CharField(db_column='Perdidas', max_length=4, blank=True, null=True)  # Field name made lowercase.
    tipo_venta = models.CharField(db_column='Tipo_Venta', max_length=20, blank=True, null=True)  # Field name made lowercase.
    id_agricultor = models.ForeignKey(Agricultores, on_delete=models.CASCADE) 

    class Meta:
        managed = False
        db_table = 'Colmenas'

def __str__(self):
        return self.cantidad

class Erosion(models.Model):
    id_erocion = models.AutoField(primary_key=True)  # Field name made lowercase.
    nombre_erocion = models.CharField(db_column='Nombre_erocion', max_length=3, blank=True, null=True)  # Field name made lowercase.
    id_agricultor = models.ForeignKey(Agricultores, on_delete=models.CASCADE) 

    class Meta:
        managed = False
        db_table = 'Erosion'

def __str__(self):
        return self.nombre_erocion

class Escolaridad(models.Model):
    id_escolaridad = models.AutoField(primary_key=True)  # Field name made lowercase.
    nombre_escolaridad = models.CharField(db_column='Nombre_escolaridad', max_length=3, blank=True, null=True)  # Field name made lowercase.
    id_agricultor = models.ForeignKey(Agricultores, on_delete=models.CASCADE) 

    class Meta:
        managed = False
        db_table = 'Escolaridad'

def __str__(self):
        return self.nombre_escolaridad

class Estanque(models.Model):
    id_estanque = models.AutoField(primary_key=True)  # Field name made lowercase.
    nombre_estanque = models.CharField(db_column='Nombre_estanque', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tipo_concreto = models.CharField(db_column='Tipo_concreto', max_length=20, blank=True, null=True)  # Field name made lowercase.
    id_agricultor = models.ForeignKey(Agricultores, on_delete=models.CASCADE) 

    class Meta:
        managed = False
        db_table = 'Estanque'

def __str__(self):
        return self.nombre_estanque

class Habita(models.Model):
    id_habita = models.AutoField(primary_key=True)  # Field name made lowercase.
    nombre_habita = models.CharField(db_column='Nombre_habita', max_length=5, blank=True, null=True)  # Field name made lowercase.
    id_agricultor = models.ForeignKey(Agricultores, on_delete=models.CASCADE) 

    class Meta:
        managed = False
        db_table = 'Habita'

def __str__(self):
        return self.nombre_habita
        

class Huertofamiliar(models.Model):
    id_guardasemillas = models.AutoField(primary_key=True)  # Field name made lowercase.
    nombre_huertofamiliar = models.CharField(db_column='Nombre_huertofamiliar', max_length=3, blank=True, null=True)  # Field name made lowercase.
    nombre_guardarsemillas = models.CharField(db_column='Nombre_guardarsemillas', max_length=3, blank=True, null=True)  # Field name made lowercase.
    id_agricultor = models.ForeignKey(Agricultores, on_delete=models.CASCADE) 

    class Meta:
        managed = False
        db_table = 'Huertofamiliar'

def __str__(self):
        return self.nombre_huertofamiliar

class Inscrita(models.Model):
    id_inscrita = models.AutoField(primary_key=True)  # Field name made lowercase.
    nombre_inscrita = models.CharField(db_column='Nombre_inscrita', max_length=3, blank=True, null=True)  # Field name made lowercase.
    id_agricultor = models.ForeignKey(Agricultores, on_delete=models.CASCADE) 

    class Meta:
        managed = False
        db_table = 'Inscrita'

def __str__(self):
        return self.nombre_inscrita

class Nativo(models.Model):
    id_nativo = models.AutoField(primary_key=True)  # Field name made lowercase.
    nombre_nativo = models.CharField(db_column='Nombre_nativo', max_length=3, blank=True, null=True)  # Field name made lowercase.
    id_agricultor = models.ForeignKey(Agricultores, on_delete=models.CASCADE) 

    class Meta:
        managed = False
        db_table = 'Nativo'

def __str__(self):
        return self.nombre_nativo

class Necesidad(models.Model):
    id_necesidad = models.AutoField(primary_key=True)  # Field name made lowercase.
    tipo_necesidad = models.CharField(db_column='Tipo_necesidad', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tipo_amenaza = models.CharField(db_column='Tipo_amenaza', max_length=200, blank=True, null=True)  # Field name made lowercase.
    id_agricultor = models.ForeignKey(Agricultores, on_delete=models.CASCADE) 

    class Meta:
        managed = False
        db_table = 'Necesidad'

def __str__(self):
        return self.tipo_necesidad

class Rubro(models.Model):
    id_rubro = models.AutoField(primary_key=True)  # Field name made lowercase.
    nombre_rubro = models.CharField(db_column='Nombre_rubro', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    id_agricultor = models.ForeignKey(Agricultores, on_delete=models.CASCADE) 

    class Meta:
        managed = False
        db_table = 'Rubro'

def __str__(self):
        return self.nombre_rubro

class Sag(models.Model):
    id_sag = models.AutoField(primary_key=True)  # Field name made lowercase.
    nombre_sag = models.CharField(db_column='Nombre_sag', max_length=5, blank=True, null=True)  # Field name made lowercase.
    id_agricultor = models.ForeignKey(Agricultores, on_delete=models.CASCADE) 

    class Meta:
        managed = False
        db_table = 'Sag'

def __str__(self):
        return self.nombre_sag

class Sector(models.Model):
    id_sector = models.AutoField(primary_key=True)  # Field name made lowercase.
    nombre_sector = models.CharField(db_column='Nombre_sector', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id_agricultor = models.ForeignKey(Agricultores, on_delete=models.CASCADE) 

    class Meta:
        managed = False
        db_table = 'Sector'

def __str__(self):
        return self.nombre_sector

class Segmento(models.Model):
    id_segmento = models.AutoField(primary_key=True)  # Field name made lowercase.
    nombre_segmento = models.CharField(db_column='Nombre_segmento', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id_agricultor = models.ForeignKey(Agricultores, on_delete=models.CASCADE) 

    class Meta:
        managed = False
        db_table = 'Segmento'

def __str__(self):
        return self.nombre_segmento

class Superficial(models.Model):
    id_superficial = models.AutoField(primary_key=True)  # Field name made lowercase.
    nombre_superficial = models.CharField(db_column='Nombre_superficial', max_length=3, blank=True, null=True)  # Field name made lowercase.
    id_agricultor = models.ForeignKey(Agricultores, on_delete=models.CASCADE) 

    class Meta:
        managed = False
        db_table = 'Superficial'

def __str__(self):
        return self.nombre_superficial

class Tenencia(models.Model):
    id_tenencia =models.AutoField(primary_key=True)  # Field name made lowercase.
    nombre_tenencia = models.CharField(db_column='Nombre_tenencia', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id_agricultor = models.ForeignKey(Agricultores, on_delete=models.CASCADE) 

    class Meta:
        managed = False
        db_table = 'Tenencia'

def __str__(self):
        return self.nombre_tenencia

class Turismo(models.Model):
    id_turismo = models.AutoField(primary_key=True)  # Field name made lowercase.
    nombre_turismo = models.CharField(db_column='Nombre_turismo', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tipo_turismo = models.CharField(db_column='Tipo_turismo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    id_agricultor = models.ForeignKey(Agricultores, on_delete=models.CASCADE) 

    class Meta:
        managed = False
        db_table = 'Turismo'

def __str__(self):
        return self.nombre_turismo

class Vertiente(models.Model):
    id_vertiente = models.AutoField(primary_key=True)  # Field name made lowercase.
    nombre_vertiente = models.CharField(db_column='Nombre_vertiente', max_length=3, blank=True, null=True)  # Field name made lowercase.
    id_agricultor = models.ForeignKey(Agricultores, on_delete=models.CASCADE) 

    class Meta:
        managed = False
        db_table = 'Vertiente'

def __str__(self):
        return self.nombre_vertiente