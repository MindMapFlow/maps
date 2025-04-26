from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from .forms import MajorForm, CourseForm

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        return redirect('home')
    return render(request, 'registration/register.html')


def create_major(request):
    if request.method == 'POST':
        form = MajorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('roadmap_home')
    else:
        form = MajorForm()
    return render(request, 'roadmap/create_major.html', {'form': form})


def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('roadmap_home')
    else:
        form = CourseForm()
    return render(request, 'roadmap/create_course.html', {'form': form})


def upload_syllabus(request):
    if request.method == 'POST':
        syllabus_file = request.FILES['syllabus_file']
        print(f"{syllabus_file.name}")
        return redirect('roadmap_home')
    return render(request, 'roadmap/upload_syllabus.html')