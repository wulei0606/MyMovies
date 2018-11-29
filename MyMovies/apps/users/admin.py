from django.contrib import admin

# Register your models here.

from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username','birthday','gender','mobile','email')
    list_filter = ('name','birthday','gender','mobile','email')
    search_fields = ('name','birthday','gender','mobile','email')

admin.site.register(UserProfile,UserProfileAdmin)