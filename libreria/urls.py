from django.urls import path
from . import views

urlpatterns = [

  

    path('login',views.login,name='login',),
    path('crear',views.crear_t,name='crear'),
    path('superad',views.superad,name='superad'),
    path('editar/<int:id>',views.editar_t,name='editar'),
    path('eliminar/<int:id>',views.eliminar_t,name='eliminar'),
    
    
    
]