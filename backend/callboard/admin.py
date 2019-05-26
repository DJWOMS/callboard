from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Category, FilterAdvert, DateAdvert, Advert


@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    """Категории"""
    list_display = ("name", "parent", "id")
    mptt_level_indent = 20
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name", "parent")


@admin.register(FilterAdvert)
class FilterAdvertAdmin(admin.ModelAdmin):
    """Фильтры"""
    list_display = ("name", "id")
    list_display_links = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)


@admin.register(DateAdvert)
class DateAdvertAdmin(admin.ModelAdmin):
    """Срок для объявления"""
    list_display = ("name", "id")
    list_display_links = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)


@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):
    """Объявления"""
    list_display = (
        "id",
        "subject",
        "user",
        "category",
        "filters",
        "date",
        "price",
        "created",
        "moderation"
    )
    list_display_links = ("subject",)
    list_filter = ("user", "category", "filters", "date", "price")
    prepopulated_fields = {"slug": ("user", "subject")}
    search_fields = ("user", "category", "subject", "date", "created")
