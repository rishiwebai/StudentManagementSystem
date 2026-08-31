from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Avg
from django.core.paginator import Paginator

from .forms import StudentForm
from .models import Student


# ==========================================
# HOME
# ==========================================

def home(request):
    total_students = Student.objects.count()

    total_courses = Student.objects.values(
        'course'
    ).distinct().count()

    average_age = Student.objects.aggregate(
        avg_age=Avg('age')
    )['avg_age']

    context = {
        'total_students': total_students,
        'total_courses': total_courses,
        'average_age': round(average_age, 1) if average_age else 0,
    }

    return render(
        request,
        'students/home.html',
        context
    )


# ==========================================
# ADD STUDENT
# ==========================================

def add_student(request):

    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('student_list')

    else:
        form = StudentForm()

    return render(
        request,
        'students/add_student.html',
        {'form': form}
    )


# ==========================================
# STUDENT LIST
# SEARCH + COURSE FILTER + PAGINATION
# ==========================================

def student_list(request):

    query = request.GET.get('q', '').strip()
    course = request.GET.get('course', '').strip()

    # Get students in fixed order
    students = Student.objects.all().order_by('id')

    # --------------------------------------
    # SEARCH
    # --------------------------------------

    if query:
        students = students.filter(
            name__icontains=query
        ) | students.filter(
            email__icontains=query
        ) | students.filter(
            phone__icontains=query
        ) | students.filter(
            course__icontains=query
        )

        # Keep pagination order after search
        students = students.order_by('id')

    # --------------------------------------
    # COURSE FILTER
    # --------------------------------------

    if course:
        students = students.filter(
            course__iexact=course
        )

    # --------------------------------------
    # COURSES FOR DROPDOWN
    # --------------------------------------

    courses = Student.objects.values_list(
        'course',
        flat=True
    ).distinct().order_by('course')

    # --------------------------------------
    # PAGINATION
    # 10 STUDENTS PER PAGE
    # --------------------------------------

    paginator = Paginator(
        students,
        10
    )

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(
        page_number
    )

    # --------------------------------------
    # CONTEXT
    # --------------------------------------

    context = {
        'students': page_obj,
        'page_obj': page_obj,
        'query': query,
        'course': course,
        'courses': courses,
    }

    return render(
        request,
        'students/student_list.html',
        context
    )


# ==========================================
# STUDENT DETAIL
# ==========================================

def student_detail(request, student_id):

    student = get_object_or_404(
        Student,
        id=student_id
    )

    return render(
        request,
        'students/student_detail.html',
        {'student': student}
    )


# ==========================================
# EDIT STUDENT
# ==========================================

def edit_student(request, student_id):

    student = get_object_or_404(
        Student,
        id=student_id
    )

    if request.method == 'POST':

        form = StudentForm(
            request.POST,
            instance=student
        )

        if form.is_valid():
            form.save()
            return redirect('student_list')

    else:

        form = StudentForm(
            instance=student
        )

    return render(
        request,
        'students/edit_student.html',
        {
            'form': form,
            'student': student
        }
    )


# ==========================================
# DELETE STUDENT
# ==========================================

def delete_student(request, student_id):

    student = get_object_or_404(
        Student,
        id=student_id
    )

    if request.method == 'POST':

        student.delete()

        return redirect('student_list')

    return render(
        request,
        'students/delete_student.html',
        {'student': student}
    )