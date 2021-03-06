from django.db import models
from django.contrib import admin
from .models import UserProfile
# Register your models here.
#admin.site.register(UserProfile )
#admin.site.site_header = 'FbCloneAdministration'


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_info', 'city', 'phone','website' )

    def user_info(self, obj):
        return obj.description

    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by('-phone', 'user')
        return queryset


    user_info.short_description = 'info'

admin.site.register(UserProfile, UserProfileAdmin)