from django.contrib import admin
from recruit_api.apps.core.user.models import User


class UserAdmin(admin.ModelAdmin):
    Queries = []
    list_display = ('id', 'email', 'username', 'is_active', 'is_superuser', 'is_staff')
    fields = ('email', 'password', 'username', 'is_active', 'is_superuser', 'is_staff')
    ordering = ('email', 'username')
    search_fields = ('email', 'username')
    list_per_page = 20


admin.site.register(User, UserAdmin)

