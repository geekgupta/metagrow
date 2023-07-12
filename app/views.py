from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import *
from .models import * 

def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/create_student.html', {'form': form})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})


def add_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_student')
    else:
        form = SubjectForm()
    return render(request, 'students/add_subject.html', {'form': form})