from django.contrib import admin

# Register your models here.

from .models import Movies,Tag,Preview

class MoviesAdmin(admin.ModelAdmin):
    list_display = ('title','url','desc','logo','star','playnum','commentunm','tag_name','area','release_time','length_time','add_time')
    list_filter = ('title','star','playnum','commentunm','tag_name','area','release_time','length_time','add_time')
    search_fields = ('title','tag_name','area')

class TagAdmin(admin.ModelAdmin):
    list_display = ('name','add_time')
    list_filter = ('name','add_time')
    search_fields = ('name','add_time')


class PreviewAdmin(admin.ModelAdmin):
    list_display = ('title','logo','add_time')
    list_filter = ('title','logo','add_time')
    search_fields = ('title','logo','add_time')

admin.site.register(Movies,MoviesAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Preview,PreviewAdmin)