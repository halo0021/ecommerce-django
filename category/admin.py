from django.contrib import admin
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('category_name',)}
    list_display=('category_name', 'slug')


#se registran las entidades o clases
admin.site.register(Category,CategoryAdmin)

