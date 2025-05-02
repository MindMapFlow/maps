from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from .forms import MajorForm, CourseForm, SyllabusForm
from .models import Course
from docx import Document

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

def normalize_text(text: str) -> str:
    return '\n'.join(line.strip() for line in text.splitlines() if line.strip())

def parse_thematic_plan(file) -> dict:
    doc = Document(file)
    result = {}
    headers = None
    last_week = None
    
    for table in doc.tables:
        if len(table.columns) == 6:
            if not headers: 
                headers = [normalize_text(cell.text).strip() for cell in table.rows[0].cells]
                start_row = 1
            else:  
                start_row = 0
            
            for row in table.rows[start_row:]:
                cells = row.cells
                if len(cells) == 6:
                    row_data = {headers[i]: normalize_text('\n'.join(p.text.strip() for p in cell.paragraphs if p.text.strip())) or "Нет данных" for i, cell in enumerate(cells)}
                    if not row_data[headers[0]] and last_week:
                        row_data[headers[0]] = last_week
                    last_week = row_data[headers[0]]
                    week_key = f"week-{row_data[headers[0]]}"
                    result[week_key] = {
                        "topic_name": row_data[headers[1]],
                        "status": False,
                        "sourse": []
                    }
    if result:
        return result
    raise ValueError("Таблица не найдена")

def upload_syllabus(request):
    syllabus_data = None
    error = None
    courses = Course.objects.all().values('id', 'name', 'major_id', 'semester')
    if request.method == 'POST':
        form = SyllabusForm(request.POST, request.FILES)
        if form.is_valid():
            syllabus_file = form.cleaned_data['syllabus_file']
            major = form.cleaned_data['major']
            semester = form.cleaned_data['semester']
            course = form.cleaned_data['course']
            try:
                thematic_plan = parse_thematic_plan(syllabus_file)
                print(thematic_plan)
                syllabus_data = {
                    'major': major.name,
                    'semester': semester,
                    'course': course.name,
                    'weeks': thematic_plan
                }
            except Exception as e:
                error = str(e)
    else:
        form = SyllabusForm()
    return render(request, 'roadmap/upload_syllabus.html', {
        'form': form,
        'syllabus_data': syllabus_data,
        'error': error,
        'courses': courses
    })