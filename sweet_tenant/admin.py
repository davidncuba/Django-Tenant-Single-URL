from sweet_tenant.models import Sweet
from django.contrib import admin

# Register your models here.
@admin.register(Sweet)
class SweetTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
