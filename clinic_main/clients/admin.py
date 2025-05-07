from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.action(description="Сделать выбранных пользователей персоналом")
def make_staff_member(modeladmin, request, queryset):
    queryset.update(is_staff_member=True)

@admin.action(description="Убрать из персонала")
def remove_from_staff(modeladmin, request, queryset):
    queryset.update(is_staff_member=False)

class StaffFilter(admin.SimpleListFilter):
    title = 'Статус персонала'
    parameter_name = 'staff_status'

    def lookups(self, request, model_admin):
        return (('staff', 'Только персонал'), ('non_staff', 'Только клиенты'),)

    def queryset(self, request, queryset):
        if self.value() == 'staff':
            return queryset.filter(is_staff_member=True)
        if self.value() == 'non_staff':
            return queryset.filter(is_staff_member=False)

class CustomUserAdmin(UserAdmin):

    actions = [make_staff_member, remove_from_staff]
    list_display = ('username', 'email', 'phone', 'is_staff_member', 'is_staff')
    list_filter = (StaffFilter,) + UserAdmin.list_filter
    #list_filter = ('is_staff_member', 'is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Персональная информация', {'fields': ('first_name', 'last_name', 'email', 'phone')}),
        ('Права доступа', {
            'fields': ('is_active', 'is_staff', 'is_staff_member', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Даты', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'phone', 'is_staff_member'),
        }),
    )
    search_fields = ('username', 'email', 'phone')
    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)