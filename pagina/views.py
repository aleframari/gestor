from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.sessions.models import Session
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User,Group
from .models import Actividad, Asignacion, Proyecto, Empresa
from .forms import ActividadForm, ProyectoForm, EmpresaForm, AsignacionForm, UsuarioForm, ProForm
# Create your views here.
def usuario_listar(request):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Usuario":
        usuarios=User.objects.all()
        return render(request, 'pagina/usuario_usuario.html', {'usuarios':usuarios,})
    else:
        return redirect('/')

def asignacion_listar(request):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Usuario":
        asignaciones = Asignacion.objects.all()
        return render(request, 'pagina/usuario_asignacion.html', {'asignaciones':asignaciones,})
    else:
        return redirect('/')

def empresa_listar(request):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Usuario":
        empresas = Empresa.objects.all()
        return render(request, 'pagina/usuario_empresa.html', {'empresas':empresas,})
    else:
        return redirect('/')

def proyecto_listar(request):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Usuario":
        proyectos = Proyecto.objects.all()
        return render(request, 'pagina/usuario_proyecto.html', {'proyectos':proyectos,})
    else:
        return redirect('/')

def actividad_listar(request):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Usuario":
        actividades = Actividad.objects.all()
        return render(request, 'pagina/usuario_actividad.html', {'actividades':actividades,})
    else:
        return redirect('/')

def borrar_usuario(request,pk):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Administrador":
        usuario = get_object_or_404(User,pk=pk)
        usuario.delete()
        return redirect('/administrador/usuarios/listar')
    else:
        return redirect('/')

def modificar_usuario(request,pk):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Administrador":
        usuario = get_object_or_404(User,pk=pk)
        if request.method=="POST":
            formulario = UsuarioForm(request.POST,instance=usuario)
            if formulario.is_valid():
                usuario = formulario.save()
                return redirect('/administrador/usuarios/listar')
        else:
            formulario=UsuarioForm(instance=usuario)
        return render(request, 'pagina/modificar_usuario.html', {'formulario':formulario})
    else:
        return redirect('/')

def agregar_usuario(request):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Administrador":
        if request.method=="POST":
            formulario = UsuarioForm(request.POST)
            if formulario.is_valid():
                if 'groups' in request.POST:
                    grupo=get_object_or_404(Group,pk=request.POST["groups"])
                    usuario = formulario.save(commit=False)
                    usuario.password = make_password(usuario.password)
                    usuario.save()
                    grupo.user_set.add(usuario)
                    return redirect('/administrador/usuarios/listar')
                else:
                    return render(request, 'pagina/agregar_usuario.html', {'formulario':formulario,'mensaje':'Se debe elegir un grupo'})
        else:
            formulario=UsuarioForm()
        return render(request, 'pagina/agregar_usuario.html', {'formulario':formulario,'mensaje':''})
    else:
        return redirect('/')

def borrar_asignacion(request,pk):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Administrador":
        asignacion = get_object_or_404(Asignacion,pk=pk)
        asignacion.delete()
        return redirect('/administrador/asignaciones/listar')
    else:
        return redirect('/')

def modificar_asignacion(request,pk):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Administrador":
        asignacion = get_object_or_404(Asignacion,pk=pk)
        if request.method=="POST":
            formulario = AsignacionForm(request.POST,instance=asignacion)
            if formulario.is_valid():
                asignacion = formulario.save()
                return redirect('/administrador/asignaciones/listar')
        else:
            formulario=AsignacionForm(instance=asignacion)
        return render(request, 'pagina/modificar_asignacion.html', {'formulario':formulario})
    else:
        return redirect('/')

def agregar_asignacion(request):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Administrador":
        if request.method=="POST":
            formulario = AsignacionForm(request.POST)
            if formulario.is_valid():
                asignacion = formulario.save()
                asignacion.save()
                return redirect('/administrador')
        else:
            formulario=AsignacionForm()
        return render(request, 'pagina/agregar_asignacion.html', {'formulario':formulario})
    else:
        return redirect('/')

def borrar_empresa(request,pk):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Administrador":
        empresa = get_object_or_404(Empresa,pk=pk)
        empresa.delete()
        return redirect('/administrador/empresa/listar')
    else:
        return redirect('/')

def modificar_empresa(request,pk):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Administrador":
        empresa = get_object_or_404(Empresa,pk=pk)
        if request.method=="POST":
            formulario = EmpresaForm(request.POST,instance=empresa)
            if formulario.is_valid():
                empresa = formulario.save()
                return redirect('/administrador/empresa/listar')
        else:
            formulario=EmpresaForm(instance=empresa)
        return render(request, 'pagina/modificar_empresa.html', {'formulario':formulario})
    else:
        return redirect('/')

def listar_empresa(request):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Administrador":
        empresas = Empresa.objects.all()
        return render(request, 'pagina/listar_empresa.html', {'empresas':empresas,})
    else:
        return redirect('/')

def agregar_empresa(request):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Administrador":
        if request.method=="POST":
            formulario = EmpresaForm(request.POST)
            if formulario.is_valid():
                empresa = formulario.save(commit=False)
                empresa.save()
                return redirect('/administrador')
        else:
            formulario=EmpresaForm()
        return render(request, 'pagina/agregar_empresa.html', {'formulario':formulario})
    else:
        return redirect('/')

def borrar_proyecto(request,pk):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Administrador":
        proyecto = get_object_or_404(Proyecto,pk=pk)
        proyecto.delete()
        return redirect('/administrador/proyecto/listar')
    else:
        return redirect('/')

def modificar_proyecto(request,pk):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Administrador":
        proyecto = get_object_or_404(Proyecto,pk=pk)
        if request.method=="POST":
            formulario = ProyectoForm(request.POST,instance=proyecto)
            if formulario.is_valid():
                proyecto = formulario.save()
                return redirect('/administrador/proyecto/listar')
        else:
            formulario=ProyectoForm(instance=proyecto)
        return render(request, 'pagina/modificar_proyecto.html', {'formulario':formulario})
    else:
        return redirect('/')

def listar_proyecto(request):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Administrador":
        proyectos = Proyecto.objects.all()
        return render(request, 'pagina/listar_proyecto.html', {'proyectos':proyectos,})
    else:
        return redirect('/')

def agregar_proyecto(request):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Administrador":
        if request.method=="POST":
            formulario = ProyectoForm(request.POST)
            if formulario.is_valid():
                proyecto = formulario.save()
                proyecto.save()
                return redirect('/administrador')
        else:
            formulario=ProyectoForm()
        return render(request, 'pagina/agregar_proyecto.html', {'formulario':formulario})
    else:
        return redirect('/')

def pelicula_nueva(request):
    if request.method == "POST":
        formulario = ProForm(request.POST)
        if formulario.is_valid():
            proyecto = Proyecto.objects.create(nombre=formulario.cleaned_data['nombre'])
            for actividad_id in request.POST.getlist('actividad'):
               actuacion = Actividad(actividad_id=actividad_id)
               actuacion.save()
               return redirect('/administrador')
    else:
        formulario = ProForm()
    return render(request, 'pagina/agregar_proyecto.html', {'formulario':formulario})

def logo(request):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Administrador":
        return render_to_response('pagina/logo.html', context_instance=RequestContext(request))
    else:
        return redirect('/')

def borrar_actividad(request,pk):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Administrador":
        actividad = get_object_or_404(Actividad,pk=pk)
        actividad.delete()
        return redirect('/administrador')
    else:
        return redirect('/')

def modificar_actividad(request,pk):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Administrador":
        actividad = get_object_or_404(Actividad,pk=pk)
        if request.method=="POST":
            formulario = ActividadForm(request.POST,instance=actividad)
            if formulario.is_valid():
                actividad = formulario.save()
                return redirect('/administrador/actividades/listar')
        else:
            formulario=ActividadForm(instance=actividad)
        return render(request, 'pagina/modificar_actividad.html', {'formulario':formulario})
    else:
        return redirect('/')

def listar_actividades(request):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Administrador":
        actividades = Actividad.objects.all()
        return render(request, 'pagina/listar_actividades.html', {'actividades':actividades,})
    else:
        return redirect('/')

def listar_asignacion_usuario(request):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Administrador":
        asignaciones = Asignacion.objects.all()
        return render(request, 'pagina/listar_asignaciones_usuario.html', {'asignaciones':asignaciones,})
    else:
        return redirect('/')

def agregar_actividad(request):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Administrador":
        if request.method=="POST":
            formulario = ActividadForm(request.POST)
            if formulario.is_valid():
                actividad = formulario.save(commit=False)
                actividad.save()
                return redirect('/administrador/actividades/listar')
        else:
            formulario=ActividadForm()
        return render(request, 'pagina/agregar_actividad.html', {'formulario':formulario})
    else:
        return redirect('/')

def listar_usuarios(request):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Administrador":
        usuarios=User.objects.all()
        return render(request, 'pagina/listar_usuarios.html', {'usuarios':usuarios,})
    else:
        return redirect('/')

def entrar(request):
    if request.user.is_authenticated():
        if len(request.user.groups.all())>0:
            if request.user.groups.all()[0].name == "Administrador":
                return redirect('/administrador')
            elif request.user.groups.all()[0].name == "Usuario":
                return redirect('/usuario')
        else:
            logout(request)
            formulario = AuthenticationForm()
            return render(request, 'pagina/login.html', {'formulario': formulario,'mensaje':'Usuario sin grupo asignado'})
    if request.method == "POST":
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            if usuario=='' or clave=='':
                formulario = AuthenticationForm()
                return render(request, 'pagina/login.html', {'formulario': formulario,'mensaje':'No se completaron todos los campos'})
            else:
                acceso = authenticate(username=usuario,password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request,acceso)
                    return redirect('/')
                else:
                    formulario = AuthenticationForm()
                    return render(request, 'pagina/login.html', {'formulario': formulario,'mensaje':'Usuario no activo'})
            else:
                formulario = AuthenticationForm()
                return render(request, 'pagina/login.html', {'formulario': formulario,'mensaje':'La combinacion de usuario y contraseña no es correcta'})
        else:
            formulario = AuthenticationForm()
            return render(request, 'pagina/login.html', {'formulario': formulario,'mensaje':'Relleno de formulario invalido'})
    else:
        formulario = AuthenticationForm()
    return render(request, 'pagina/login.html', {'formulario': formulario,'mensaje':''})

def abandonar(request):
    logout(request)
    return redirect('/')

def administrador(request):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Administrador":
        usuario = request.user
        return render(request, 'pagina/administrador.html', {'usuario':usuario,})
    else:
        return redirect('/')

def usuario(request):
    if len(request.user.groups.all())>0 and request.user.groups.all()[0].name == "Usuario":
        usuario = request.user
        return render(request, 'pagina/usuario.html', {'usuario':usuario,})
    else:
        return redirect('/')
