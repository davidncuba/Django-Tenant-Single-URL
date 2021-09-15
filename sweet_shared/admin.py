from sweet_shared.models import SweetType
from django.contrib import admin

# Register your models here.
@admin.register(SweetType)
class SweetTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
