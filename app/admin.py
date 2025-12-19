from django.contrib import admin
from .models import TechCategory, Appliance

@admin.register(Appliance)
class ApplianceAdmin(admin.ModelAdmin):
    # Используем appliance_name вместо name
    list_display = ['appliance_name', 'category', 'tech_type', 'created_at_short']
    list_filter = ['category', 'tech_type', 'created_at']
    search_fields = ['appliance_name', 'description']
    autocomplete_fields = ['category']
    date_hierarchy = 'created_at'
    
    # Поля только для чтения
    readonly_fields = ['created_at', 'updated_at']
    
    # Группировка полей
    fieldsets = (
        ('Основная информация', {
            'fields': ('appliance_name', 'category', 'description', 'image')
        }),
        ('Технические характеристики', {
            'fields': (
                'tech_type', 
                'print_type', 
                'print_technique',
                'placement',
                'productivity'
            )
        }),
        ('Характеристики печати', {
            'fields': (
                'double_print',
                'print_resolution',
                'print_speed',
                'warm_up_time',
                'first_print_time'
            )
        }),
        ('Сканер', {
            'fields': ('scanner_type',)
        }),
        ('Служебные данные', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)  # сворачиваемый блок
        })
    )
    
    def created_at_short(self, obj):
        return obj.created_at.strftime('%d.%m.%Y')
    created_at_short.short_description = 'Дата создания'


@admin.register(TechCategory)
class TechCategoryAdmin(admin.ModelAdmin):
    # Убираем 'id', так как его нет (primary_key - это category_name)
    list_display = ['category_name', 'get_appliance_count']
    search_fields = ['category_name']
    
    def get_appliance_count(self, obj):
        # Используем related_name из модели Appliance
        return obj.tech_items.count()  # tech_items - это related_name
    get_appliance_count.short_description = 'Количество техники'