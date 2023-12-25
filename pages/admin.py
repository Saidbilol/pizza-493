from django.contrib import admin

from .models import ScrollModel, GallaryModel, MenuModel


@admin.register(ScrollModel)
class ScrollModelAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "discount", "created_at"]
    search_fields = ["title", "description"]
    list_filter = ["created_at", "updated_at"]
    ordering = ["-created_at"]


@admin.register(GallaryModel)
class ScrollModelAdmin(admin.ModelAdmin):
    list_display = ["id", "created_at"]
    list_filter = ["created_at", "updated_at"]
    ordering = ["-created_at"]


@admin.register(MenuModel)
class ScrollModelAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "price", "created_at"]
    list_filter = ["created_at", "updated_at"]
    ordering = ["-created_at"]
