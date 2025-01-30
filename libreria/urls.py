from django.urls import path
from . import views
from django.conf import settings 



urlpatterns = [
    path('login', views.login, name='login'),
    path('superad', views.superad, name='superad'),
    path('pricing', views.pricing, name='pricing'),
    path('base', views.base_logins, name='base'),
    path('crear_usuario', views.crear_usuario, name='crear_usuario'),
    path('lista_usuarios', views.lista_usuarios, name='lista_usuarios'),
    path('crear_empresa', views.crear_empresa, name='crear_empresa'),
    path('crear_permiso', views.crear_permisos, name='crear_permiso'),
    path('lista_permisos', views.lista_permisos, name='lista_permisos'),
    path('relacionar_empresa_supervisor', views.relacionar_empresa_supervisor, name='relacionar_empresa_supervisor'),
    path('ver_supervisores_trabajadores/<int:empresa_id>', views.ver_supervisores_trabajadores, name='ver_supervisores_trabajadores'),
    path('lista_empresas', views.lista_empresas, name='lista_empresas'),
    path('lista_empresas_detalles', views.lista_empresas_detalles, name='lista_empresas_detalles'),
    path('eliminar_empresa/<int:empresa_id>', views.eliminar_empresa, name='eliminar_empresa'),
    path('añadir_trabajador/<int:empresa_id>', views.crear_usuario, name='añadir_trabajador'),
    path('relacionar_empresa_supervisor/<int:empresa_id>', views.relacionar_empresa_supervisor, name='añadir_supervisor'),
    path('editar_supervisor/<int:id>', views.editar_supervisor, name='editar_supervisor'),
    path('eliminar_supervisor/<int:id>', views.eliminar_supervisor, name='eliminar_supervisor'),
    path('editar_t/<int:id>', views.editar_t, name='editar_t'),
    path('eliminar_t/<int:id>', views.eliminar_t, name='eliminar_t'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)