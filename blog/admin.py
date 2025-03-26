from django.contrib import admin

from blog.models import Blog, Category

# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "favourite",]
    list_editable = ("favourite",)
    search_fields = ("title", "description")
    readonly_fields = ("slug",)
    list_filter = ["categories"]



@admin.register(Category)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name","slug")
    

