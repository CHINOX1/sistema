from django.urls import path
from . import views
from django.conf import settings 



urlpatterns = [
    path('login',views.login,name='login',),
    path('crear',views.crear_t,name='crear'),
    path('superad',views.superad,name='superad'),
    path('editar/<int:id>',views.editar_t,name='editar'),
    path('eliminar/<int:id>',views.eliminar_t,name='eliminar'),
    path('pricing',views.pricing,name='pricing'),
    path('base',views.base_logins,name='base'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)