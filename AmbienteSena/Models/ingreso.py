from django.utils import timezone
from django.db import models

class Ingreso(models.Model):
    instructor = models.ForeignKey('AmbienteSena.Instructor', on_delete=models.RESTRICT)
    ambiente = models.ForeignKey('AmbienteSena.Ambiente',on_delete=models.RESTRICT)
    fechaHoraEntrada = models.DateTimeField(default=timezone.now)
    fechaHoraSalida = models.DateTimeField(null=True, blank=True)
    observacion = models.TextField(blank=True)
    class Meta:
        db_table = 'ingreso'
        