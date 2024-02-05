from django.contrib import admin
from app.models import *

# Register your models here.

class customwebpage(admin.ModelAdmin):
    list_display = ['topic_name','name','url','email']
    list_display_links = ['url' ]
    list_editable = [ 'name','email']
    list_filter = ['name']
    



admin.site.register(Topic)

admin.site.register(Webpage,customwebpage )
admin.site.register(Accessrecord)

admin.site.site_header='new project'
admin.site.site_title='abcd'
admin.site.index_title='new things'





