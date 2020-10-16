from django.contrib import admin
from .models import Team
from django.utils.html import format_html

# Register your models here.
class TeamAdmin(admin.ModelAdmin):

    # show image in admin panel
    def thumbnail(self,object):
        return format_html("<img src='{}' width='35' style='border-radius:17.5px;' />".format(object.photo.url))
    
    thumbnail.short_description = 'image'

    list_display = ('id', 'thumbnail' ,'first_name','last_name','designation','craeted_date')
    list_display_links = ('id','first_name','last_name')
    search_fields = ('id','first_name','last_name')
    list_filter = ('designation',)

admin.site.register(Team,TeamAdmin)