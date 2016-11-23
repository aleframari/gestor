from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^administrador$', views.administrador),
        #url(r'^/usuario$', views.usuario),
        url(r'^$', views.entrar),
        url(r'^abandonar$', views.abandonar),

        url(r'^administrador/actividades/ingreso$', views.agregar_actividad),
        url(r'^administrador/actividades/borrar/(?P<pk>[0-9]+)$', views.borrar_actividad),
        url(r'^administrador/actividades/modificar/(?P<pk>[0-9]+)$', views.modificar_actividad),
        url(r'^administrador/actividades/listar$', views.listar_actividades),

        url(r'^administrador/proyecto/ingreso$', views.agregar_proyecto),
        url(r'^administrador/proyecto/listar$', views.listar_proyecto),
        url(r'^administrador/proyecto/modificar/(?P<pk>[0-9]+)$', views.modificar_proyecto),
        url(r'^administrador/proyecto/borrar/(?P<pk>[0-9]+)$', views.borrar_proyecto),

        url(r'^administrador/empresa/ingreso$', views.agregar_empresa),
        url(r'^administrador/empresa/listar$', views.listar_empresa),
        url(r'^administrador/empresa/modificar/(?P<pk>[0-9]+)$', views.modificar_empresa),
        url(r'^administrador/empresa/borrar/(?P<pk>[0-9]+)$', views.borrar_empresa),

        url(r'^administrador/asignaciones/ingreso$', views.agregar_asignacion),
        url(r'^administrador/asignaciones/listar$', views.listar_asignacion_usuario),
        url(r'^administrador/asignaciones/modificar/(?P<pk>[0-9]+)$', views.modificar_asignacion),
        url(r'^administrador/asignaciones/borrar/(?P<pk>[0-9]+)$', views.borrar_asignacion),

        url(r'^administrador/usuario/ingreso$', views.agregar_usuario),
        url(r'^administrador/usuarios/listar$', views.listar_usuarios),
        url(r'^administrador/usuario/modificar/(?P<pk>[0-9]+)$', views.modificar_usuario),
        url(r'^administrador/usuario/borrar/(?P<pk>[0-9]+)$', views.borrar_usuario),

        url(r'^usuario/asignaciones/listar$', views.listar_asignacion_usuario),

        url(r'^usuario$', views.usuario),
        url(r'^usuario/actividades/listar$', views.actividad_listar),
        url(r'^usuario/proyecto/listar$', views.proyecto_listar),
        url(r'^usuario/empresa/listar$', views.empresa_listar),
        url(r'^usuario/asignacion/listar$', views.asignacion_listar),
        url(r'^usuario/usuario/listar$', views.usuario_listar),
    ]
