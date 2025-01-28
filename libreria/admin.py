from django.contrib import admin
from .models import Trabajador, Profile
#profile detallado
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'address', 'location', 'phone', 'user_groups']
    search_fields = ['locarion', 'user__username', 'user__groups__name']
    list_filter = ['user__groups', 'location' ]

    def user_groups(self, obj):
        return " - ".join([g.name for g in obj.user.groups.all().order_by('name')])
    
    user_groups.short_description = 'Grupos'
    

admin.site.register(Profile,ProfileAdmin)
admin.site.register(Trabajador)


