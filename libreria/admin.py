from django.contrib import admin
from .models import Trabajador, Profile
#profile detallado
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'nombre', 'apellido', 'email', 'telefono', 'pais', 'ciudad', 'region', 'direccion']
    search_fields = ['user__username', 'user__groups__name', 'pais', 'ciudad', 'region']
    list_filter = ['user__groups', 'ciudad', 'region', 'pais', ]

    def user_groups(self, obj):
        return " - ".join([g.name for g in obj.user.groups.all().oreder_by('name')])
    
    user_groups.short_description = 'Grupos'
    

admin.site.register(Profile,ProfileAdmin)
admin.site.register(Trabajador)


