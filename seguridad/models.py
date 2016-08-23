from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Proyecto(models.Model):
    id_proyecto = models.AutoField(primary_key=True, db_column='ID_PROYECTO')
    sigla_proy = models.CharField(db_column='SIGLA_PROY', max_length=20, blank=True, null=True)
    anio_proy = models.CharField(db_column='ANIO_PROY', max_length=4, blank=True, null=True)
    des_proy = models.CharField(db_column='DES_PROY', max_length=60, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s , %s' %(self.id_proyecto,self.sigla_proy)

    class Meta:
        managed = True
        db_table = 'PROYECTO'


class Sistema(models.Model):
    id_sistema = models.AutoField(primary_key=True, db_column='ID_SISTEMA')
    des_sist = models.CharField(db_column='DES_SIST', max_length=100, blank=True, null=True)
    nom_sist = models.CharField(db_column='NOM_SIST', max_length=50, blank=True, null=True)
    proyectos = models.ManyToManyField(Proyecto, through='ProyectoSistema')
    create_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s , %s' %(self.id_sistema, self.nom_sist)

    class Meta:
        managed = True
        db_table = 'SISTEMA'


class ProyectoSistema(models.Model):
    id_proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='proyectos')
    id_sistema = models.ForeignKey(Sistema, on_delete=models.CASCADE, related_name='sistemas')
    create_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s , %s' % (self.id_proyecto, self.id_sistema)

    class Meta:
        managed = True
        db_table = 'PROYECTO_SISTEMA'
        unique_together = (('id_proyecto', 'id_sistema'))


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True, db_column='ID_USUARIO')
    dni = models.CharField(db_column='DNI', max_length=8)
    ape_pat_per = models.CharField(db_column='APE_PAT_PER', max_length=35, blank=True, null=True)
    ape_mat_per = models.CharField(db_column='APE_MAT_PER', max_length=35, blank=True, null=True)
    nom_emp_per = models.CharField(db_column='NOM_EMP_PER', max_length=35, blank=True, null=True)
    fec_nac_per = models.DateTimeField(db_column='FEC_NAC_PER', blank=True, null=True)  # Field name made lowercase.
    email_insti = models.CharField(db_column='EMAIL_INSTI', max_length=50, blank=True, null=True)
    sex_emp_per = models.CharField(db_column='SEX_EMP_PER', max_length=1, blank=True, null=True)
    usuario = models.CharField(db_column='USUARIO', max_length=20, blank=True, null=True)
    proyectos_sistemas = models.ManyToManyField(ProyectoSistema, through='UsuarioProyectoSistema')

    def __unicode__(self):
        return '%s , %s' %(self.dni, self.nom_emp_per)

    class Meta:
        managed = True
        db_table = 'USUARIO'



class UsuarioProyectoSistema(models.Model):
    id_proyectosistema = models.ForeignKey(ProyectoSistema, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __unicode__(self):
        return '%s , %s' %(self.id_proyectosistema, self.id_usuario)

    class Meta:
        managed = True
        db_table = 'USUARIO_PROYECTO_SISTEMA'
        unique_together = (('id_usuario','id_proyectosistema'))
