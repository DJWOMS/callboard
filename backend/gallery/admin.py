from django.contrib import admin

from .models import Gallery, Photo


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    """Галерея"""
    list_display = ("name", "created", "id")
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ("name", "created")
    search_fields = ("name", "created")


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    """Изображения"""
    list_display = ("name", "created", "id")
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ("name", "created")
    search_fields = ("name", "created")
