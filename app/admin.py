from django.contrib import admin
from .models import audit_log, Subscription, SubscriptionFeature, Product, ProductFeature


# --- Inline для возможностей ---

class SubscriptionFeatureInline(admin.TabularInline):
    model = SubscriptionFeature
    extra = 1
    ordering = ["order"]


class ProductFeatureInline(admin.TabularInline):
    model = ProductFeature
    extra = 1
    ordering = ["order"]


# --- Подписки ---

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "order", "is_active"]
    list_editable = ["order", "is_active"]
    list_filter = ["is_active"]
    search_fields = ["name", "description"]
    inlines = [SubscriptionFeatureInline]
    fieldsets = (
        (None, {
            "fields": ("name", "image", "price", "description", "order", "is_active"),
        }),
        ("Дополнительная информация", {
            "fields": ("type_label", "payment_period", "min_term", "support"),
        }),
    )


# --- Товары ---

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "order", "is_active"]
    list_editable = ["order", "is_active"]
    list_filter = ["is_active"]
    search_fields = ["name", "description"]
    inlines = [ProductFeatureInline]
    fieldsets = (
        (None, {
            "fields": ("name", "image", "price", "description", "order", "is_active"),
        }),
        ("Дополнительная информация", {
            "fields": ("type_label", "format_field", "warranty"),
        }),
    )


admin.site.register(audit_log)
