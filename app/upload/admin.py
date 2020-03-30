from django.contrib import admin
from .models import Type1, Type2, Type3, Type4, Type5, Type6, Type7, Type8


@admin.register(Type1)
class Type1(admin.ModelAdmin):
    list_display = "Booking_ID", "Check_In", "Check_Out",
    list_filter = "Check_In", "Check_Out",


@admin.register(Type8)
class Type8Admin(admin.ModelAdmin):
    list_display = [field.name for field in Type8._meta.get_fields()]


admin.site.register(Type2)
admin.site.register(Type3)
admin.site.register(Type4)
admin.site.register(Type5)
admin.site.register(Type6)
admin.site.register(Type7)
