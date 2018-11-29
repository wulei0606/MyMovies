from django.contrib import admin

# Register your models here.
from .models import Comment,Moviecol

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user','movie','content','add_time')
    list_filter = ('user','movie','content','add_time')
    search_fields = ('user','movie','content','add_time')

class MoviecolAdmin(admin.ModelAdmin):
    list_display = ('user','movie','add_time')
    list_filter = ('user','movie','add_time')
    search_fields = ('user','movie','add_time')

admin.site.register(Comment,CommentAdmin)
admin.site.register(Moviecol,MoviecolAdmin)