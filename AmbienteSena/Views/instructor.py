from django.contrib import messages
from django.shortcuts import redirect, render
from AmbienteSena.Models.instructor import Instructor


def RegistrarInstructor(request):
    if request.method == 'POST':
        if request.POST.get('nombre') and request.POST.get('area') and request.POST.get('celular') and request.POST.get('cedula'):
            try:
                instructor = Instructor()
                instructor.NombreCompleto = request.POST.get('nombre')
                instructor.Area = request.POST.get('area')
                instructor.Celular = request.POST.get('celular')
                instructor.Cedula = request.POST.get('cedula')
                instructor.save()
                messages.success(request,"Instructor Registrado Correctamente")
            except Exception as e:
                messages.error(request, "Ocurrio un error en el sistema. Intenlo mas tarde {{ e }}")
            return redirect('/Instructores/ListarInstructores')
    else:
        return render(request,'Instructores/RegistrarInstructor.html')
    

###METODO PARA LISTAR INSTRUCTORES ###
def ListarInstructores(request):
    try:
        listadoInstructores = Instructor.objects.all().order_by('-id')
        return render(request, 'Instructores/ListarInstructores.html',
                      {'listadoInstructores':listadoInstructores})
    except Exception as e:
        messages.error(request,"Ocurrio un error en el sistema. Intenlo mas tarde {{ e }}")
    return render(request, 'Instructores/ListarInstructores.html',
                      {'listadoInstructores':listadoInstructores})

###METODO PARA ELIMINAR INSTRUCTORES ###
def EliminarInstructor(request):
    if request.method == 'POST':
        try:
            instructor = Instructor.objects.get(id = request.POST.get('id'))
            instructor.delete()
            messages.success(request,'Instrcutor Eliminado Correctamente')
        except Exception as e:
            messages.error(request,f'Ocurrio un error en el sistema. Intenlo mas tarde { e }')
        return redirect('/Instructores/ListarInstructores')

###METODO PARA ACTUALIZAR INSTRUCTORES ###
def ActualizarInstructor(request, id_instructor):
    if request.method == 'POST':
        if request.POST.get('nombre') and request.POST.get('area') and request.POST.get('celular') and request.POST.get('cedula'):
            try:
                 instructor = Instructor.objects.get(id=id_instructor)
                 instructor.NombreCompleto = request.POST.get('nombre')
                 instructor.Area = request.POST.get('area')
                 instructor.Cedula = request.POST.get('cedula')
                 instructor.Celular = request.POST.get('celular')
                 instructor.save()
                 messages.success(request,'Instructor Actualizado Correctamente')
            except Exception as e:
                messages.error(request,f'Ocurrio un error en el sistema. Intenlo mas tarde { e }')
            return redirect('/Instructores/ListarInstructores')
        else:
            messages.error(request, 'Falta Diligenciar un Campo.')
            return redirect('/Instructores/ListarInstructores')
    else:            
        try:
            instructor = Instructor.objects.filter(id = id_instructor)
            return render(request, 'Instructores/ActualizarInstructor.html',{'instructor':instructor})
        except Exception as e:
            messages.error(request,f'Ocurrio un error en el sistema. Intenlo mas tarde { e }')
            return redirect('/Instructores/ListarInstructores')
    
