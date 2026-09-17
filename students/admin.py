from django.contrib import admin
from .models import Student

# Customize Django Admin Header and Titles
admin.site.site_header = "Student Management System Admin Portal"
admin.site.site_title = "Student MS Admin Portal"
admin.site.index_title = "Lineysha & Thevan Software Technologies • Database Admin"


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_number', 'email', 'course', 'phone', 'created_at')
    search_fields = ('name', 'roll_number', 'email', 'course', 'phone')
    list_filter = ('course', 'created_at')
    ordering = ('roll_number',)
    list_per_page = 20
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ("Student Identification", {
            "fields": ("name", "roll_number"),
            "description": "Core identity details of the student."
        }),
        ("Academic Program", {
            "fields": ("course",),
            "description": "Degree program enrollment."
        }),
        ("Contact Details", {
            "fields": ("email", "phone"),
            "description": "Official communication channels."
        }),
        ("Audit Timestamps", {
            "fields": ("created_at", "updated_at"),
            "classes": ("collapse",),
            "description": "System generated record timestamps."
        }),
    )


