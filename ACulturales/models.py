from django.db import models

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=50, verbose_name="nombre")

    class Meta:
        db_table = "categoria"
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ["nombre_categoria"]

    def __str__(self):
        return '%s' % (self.nombre_categoria)
 


class AmbitoCultural(models.Model):
    id_ambito = models.AutoField(primary_key=True)
    nombre_ambito = models.CharField(max_length=70, verbose_name="nombre")

    class Meta:
        db_table = "ambito_cultural"
        verbose_name = "Ambito Cultural"
        verbose_name_plural = "Ambitos Culturales"
        ordering = ["nombre_ambito"]

    def __str__(self):
        return '%s' % (self.nombre_ambito)


class Parroquia(models.Model):
    id_parroquia = models.AutoField(primary_key=True)
    nombre_parroquia = models.CharField(max_length=50, verbose_name="nombre")
    nombre_presidente = models.CharField(max_length=60, verbose_name="presidente")
    direccion_parroquia = models.CharField(max_length=60, verbose_name="direccion GAD")
    telefono_parroquia = models.CharField(max_length=10, verbose_name="telefono GAD")
    correo_parroquia = models.CharField(max_length=50, verbose_name="correo GAD")

    class Meta:
        db_table = "parroquia"
        verbose_name = "Parroquia"
        verbose_name_plural = "Parroquias"
        ordering = ["nombre_parroquia"]

    def __str__(self):
        return '%s' % (self.nombre_parroquia)


class Agrupacion(models.Model):
    id_agrupacion = models.AutoField(primary_key=True)
    parroquia = models.ForeignKey('Parroquia', models.DO_NOTHING, related_name="parroquia", db_column='id_parroquia', blank=True, null=True)
    ambito = models.ForeignKey('AmbitoCultural', models.DO_NOTHING, related_name="ambito", db_column='id_ambito', blank=True, null=True)
    categoria = models.ForeignKey('Categoria', models.DO_NOTHING, related_name="categoria", db_column='id_categoria', blank=True, null=True)
    nombre_agrupacion = models.CharField(max_length=60, verbose_name="nombre")
    nombre_contacto = models.CharField(max_length=60, verbose_name="nombre Contacto")
    telefono_contacto = models.CharField(max_length=10, verbose_name="telefono")
    direccion_agrupacion = models.CharField(max_length=200, blank=True, null=True, verbose_name="direccion")
    ruc = models.CharField(max_length=13, blank=True, null=True, verbose_name="ruc")
    correo_agrupacion = models.CharField(max_length=50, blank=True, null=True, verbose_name="correo")
    observacion = models.CharField(max_length=200, null=True, verbose_name="observacion")
    tipo = models.CharField(max_length=1, verbose_name="tipo")

    class Meta:
        db_table = "agrupacion"
        verbose_name = "Agrupacion"
        verbose_name_plural = "Agrupaciones"
        ordering = ["nombre_agrupacion"]

    def __str__(self):
        return '%s, %s, %s, %s' % (self.nombre_agrupacion,
                                    self.telefono_contacto,
                                    self.correo_agrupacion,
                                    self.tipo)


# class Artista(models.Model):
#     id_artista = models.AutoField(primary_key=True)
#     id_agrupacion = models.ForeignKey(Agrupacion, related_name="grupo", db_column='id_agrupacion', blank=True, null=True, on_delete=models.CASCADE)
#     nombre_artista = models.CharField(max_length=60)
#     direccion_artista = models.CharField(max_length=200)
#     correo_artista = models.CharField(max_length=50, blank=True, null=True)
#     telefono_artista = models.CharField(max_length=10)

#     def __str__(self):
#         return '%s, %s, %s' % (self.nombre_artista,
#                                    self.correo_artista,
#                                    self.telefono_artista)

# class Talento(models.Model):
#     id_talento = models.AutoField(primary_key=True)
#     nombre_talento = models.CharField(max_length=50)
#     artistas = models.ManyToManyField(Artista, related_name="artistas")


#     def __str__(self):
#         return '%s' % (self.nombre_talento)

