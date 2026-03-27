from django.shortcuts import redirect, render
from django.contrib import messages
from django.utils import timezone

from ..Models.instructor import Instructor
from ..Models.ambiente import Ambiente
from ..Models.ingreso import Ingreso


def RegistrarIngreso(request):
    if request.method == 'POST':
        if request.POST.get('instructor') and request.POST.get('ambiente'):
            try:
                ingreso = Ingreso(
                    instructor_id = request.POST.get('instructor'),
                    ambiente_id = request.POST.get('ambiente'),
                    observacion = request.POST.get('observacion')         
                )
                ingreso.save()
                messages.success(request,'Ingreso Registrado Correctamente')
            except Exception as e:
                messages.error(request,'Ocurrio un Error en el Sistema')
        else:
            messages.warning(request,'Debe Seleccionar un Instructor y un Ambiente de Formación')
        return redirect('/Ingreso/ListarIngresos')
    else:
        listadoInstructores = Instructor.objects.all().order_by('NombreCompleto')
        listadoAmbientes = Ambiente.objects.all().order_by('NombreAmbiente')
        return render(request,'Ingreso/RegistrarIngreso.html',{'instructores':listadoInstructores,'ambientes': listadoAmbientes})
    
###LISTADO DE INGRESOS###
def ListarIngresos(request):
    listadoIngresos = Ingreso.objects.filter(fechaHoraSalida__isnull=True).select_related("instructor", "ambiente")
    return render(request,'Ingreso/ListarIngresos.html',{'ingresos':listadoIngresos})

###REGISTRAR SALIDA###
def RegistrarSalida(request):
    if request.method == 'POST':
        if request.POST.get('id'):
            try:
                ingreso = Ingreso.objects.get(id=request.POST.get('id'))
                ingreso.fechaHoraSalida = timezone.now()
                ingreso.save()
                messages.success(request,'Salida Registrada Correctamente')
            except Exception as e:
                messages.error(request,'Ocurrio un Error en el Sistema')
        else:
            messages.warning(request,'No Tiene Entradas Registradas')
        return redirect('/Ingreso/ListarIngresos')
