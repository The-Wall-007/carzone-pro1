from django.contrib import admin
from .models import Car
from django.utils.html import format_html


# Register your models here.
class CarAdmin(admin.ModelAdmin):
    
    # show image in admin panel
    def thumbnail(self,object):
        return format_html("<img src='{}' width='35' style='border-radius:17.5px;' />".format(object.car_photo.url))
    thumbnail.short_description = 'image'

    list_display = (
        'id',
        'car_title',
        'thumbnail',
        'color',
        'model',
        'year',
        'price',
        'is_featured',        
    )
    list_display_links = (
        'car_title',
        'thumbnail',
        'color',
        'model',
    )   
    list_editable= ('is_featured',) 
    search_fields = ('id','car_title','model')
    list_filter = ('car_title',)
    # ordering = ('id')

admin.site.register(Car,CarAdmin)