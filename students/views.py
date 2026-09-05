from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.views.decorators.http import require_http_methods
from .models import Student
from .forms import StudentForm


def dashboard_view(request):
    """
    Renders the dashboard with live database statistics and recent student records.
    """
    total_students = Student.objects.count()
    courses_count = Student.objects.values('course').distinct().count() if total_students > 0 else 0
    records_count = total_students
    from django.db import connection
    db_engine = connection.settings_dict.get('ENGINE', '')
    database_name = "PostgreSQL" if 'postgres' in db_engine else "SQLite"
    
    recent_students = Student.objects.all()[:5]
    
    context = {
        'total_students': total_students,
        'courses_count': courses_count,
        'records_count': records_count,
        'database_name': database_name,
        'recent_students': recent_students,
        'active_page': 'dashboard',
    }
    return render(request, 'dashboard.html', context)


def student_list_view(request):
    """
    Renders the student records list with multi-field search and pagination.
    """
    search_query = request.GET.get('q', '').strip()
    
    students_queryset = Student.objects.all()
    if search_query:
        students_queryset = students_queryset.filter(
            Q(name__icontains=search_query) |
            Q(roll_number__icontains=search_query) |
            Q(email__icontains=search_query) |
            Q(course__icontains=search_query) |
            Q(phone__icontains=search_query)
        )
    
    # 8 records per page for smooth and easily demonstrable pagination
    paginator = Paginator(students_queryset, 8)
    page = request.GET.get('page', 1)
    
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        students = paginator.page(1)
    except EmptyPage:
        students = paginator.page(paginator.num_pages)
        
    context = {
        'students': students,
        'search_query': search_query,
        'total_count': paginator.count,
        'active_page': 'students',
    }
    return render(request, 'students/student_list.html', context)


def student_detail_view(request, pk):
    """
    Renders the profile view of a specific student.
    """
    student = get_object_or_404(Student, pk=pk)
    context = {
        'student': student,
        'active_page': 'students',
    }
    return render(request, 'students/student_detail.html', context)


def student_create_view(request):
    """
    Handles adding a new student record.
    """
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            messages.success(request, "Student added successfully.")
            return redirect('students:student_list')
        else:
            messages.error(request, "Please correct the errors in the form below.")
    else:
        form = StudentForm()
        
    context = {
        'form': form,
        'page_title': 'Add Student',
        'page_subtitle': 'Enter student details to add them to the database',
        'submit_button_text': 'Save Student',
        'is_edit': False,
        'active_page': 'student_add',
    }
    return render(request, 'students/student_form.html', context)


def student_update_view(request, pk):
    """
    Handles updating an existing student record.
    """
    student = get_object_or_404(Student, pk=pk)
    
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student record updated successfully.")
            return redirect('students:student_detail', pk=student.pk)
        else:
            messages.error(request, "Please correct the errors in the form below.")
    else:
        form = StudentForm(instance=student)
        
    context = {
        'form': form,
        'student': student,
        'page_title': 'Edit Student',
        'page_subtitle': 'Update student details in the database',
        'submit_button_text': 'Update Student',
        'is_edit': True,
        'active_page': 'students',
    }
    return render(request, 'students/student_form.html', context)


@require_http_methods(["POST"])
def student_delete_view(request, pk):
    """
    Handles safe deletion of a student record via POST request.
    """
    student = get_object_or_404(Student, pk=pk)
    student_name = student.name
    student.delete()
    messages.success(request, "Student record deleted successfully.")
    return redirect('students:student_list')
