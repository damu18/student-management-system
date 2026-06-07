from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q, Avg
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from .models import Student
from .forms import StudentForm

def student_list(request):
    queryset = Student.objects.all().order_by('-created_at')
    
    # Statistics calculations on unfiltered data
    total_students = Student.objects.count()
    
    avg_marks = Student.objects.aggregate(Avg('marks'))['marks__avg']
    avg_marks = round(avg_marks, 2) if avg_marks is not None else 0.0
    
    pass_count = Student.objects.filter(marks__gte=40).count()
    pass_rate = round((pass_count / total_students) * 100, 1) if total_students > 0 else 0.0
    
    top_student = Student.objects.order_by('-marks').first()
    
    # Apply search and filters
    search_query = request.GET.get('q', '').strip()
    class_filter = request.GET.get('class_name', '').strip()
    gender_filter = request.GET.get('gender', '').strip()
    performance_filter = request.GET.get('performance', '').strip()
    
    if search_query:
        queryset = queryset.filter(
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query) |
            Q(roll_number__icontains=search_query) |
            Q(email__icontains=search_query) |
            Q(mobile_no__icontains=search_query)
        )
        
    if class_filter:
        queryset = queryset.filter(class_name=class_filter)
        
    if gender_filter:
        queryset = queryset.filter(gender=gender_filter)
        
    if performance_filter:
        if performance_filter == 'excellent':
            queryset = queryset.filter(marks__gte=80)
        elif performance_filter == 'good':
            queryset = queryset.filter(marks__gte=60, marks__lt=80)
        elif performance_filter == 'pass':
            queryset = queryset.filter(marks__gte=40, marks__lt=60)
        elif performance_filter == 'fail':
            queryset = queryset.filter(marks__lt=40)
            
    # Get distinct class names for filter dropdown
    class_names = Student.objects.values_list('class_name', flat=True).distinct().order_by('class_name')
    
    # Pagination
    paginator = Paginator(queryset, 8)  # 8 students per page
    page = request.GET.get('page', 1)
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        students = paginator.page(1)
    except EmptyPage:
        students = paginator.page(paginator.num_pages)
        
    context = {
        'students': students,
        'total_students': total_students,
        'avg_marks': avg_marks,
        'pass_rate': pass_rate,
        'top_student': top_student,
        'class_names': class_names,
        'q': search_query,
        'class_filter': class_filter,
        'gender_filter': gender_filter,
        'performance_filter': performance_filter,
    }
    return render(request, 'user/student_list.html', context)

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    # Calculate grade status
    if student.marks >= 80:
        grade = 'Excellent'
        grade_class = 'badge-success'
    elif student.marks >= 60:
        grade = 'Good'
        grade_class = 'badge-primary'
    elif student.marks >= 40:
        grade = 'Pass'
        grade_class = 'badge-warning'
    else:
        grade = 'Fail'
        grade_class = 'badge-danger'
        
    return render(request, 'user/student_detail.html', {
        'student': student,
        'grade': grade,
        'grade_class': grade_class
    })

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            messages.success(request, f'Student {student.first_name} {student.last_name} added successfully!')
            return redirect('student_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = StudentForm()
    return render(request, 'user/student_form.html', {'form': form, 'action': 'Add New'})

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            messages.success(request, f'Student {student.first_name} {student.last_name} updated successfully!')
            return redirect('student_detail', pk=student.pk)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = StudentForm(instance=student)
    return render(request, 'user/student_form.html', {'form': form, 'action': 'Edit', 'student': student})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        name = f"{student.first_name} {student.last_name}"
        student.delete()
        messages.success(request, f'Student {name} deleted successfully.')
        return redirect('student_list')
    return render(request, 'user/student_confirm_delete.html', {'student': student})

