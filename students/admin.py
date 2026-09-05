from django.contrib import admin
from .models import Student

# Customize Django Admin Header and Titles
admin.site.site_header = "Student Management System Admin"
admin.site.site_title = "Student MS Admin Portal"
admin.site.index_title = "Database Administration • Lineysha & Thevan Software Technologies"


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_number', 'email', 'course', 'phone', 'created_at')
    search_fields = ('name', 'roll_number', 'email', 'course', 'phone')
    list_filter = ('course', 'created_at')
    ordering = ('-created_at',)
    list_per_page = 20


