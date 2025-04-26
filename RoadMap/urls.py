from django.urls import path
from django.views.generic import TemplateView
from .views import register, create_major, create_course, upload_syllabus

urlpatterns = [
    path('', TemplateView.as_view(template_name='roadmap/home.html'), name='roadmap_home'),
    path('register/', register, name='register'),
    path('create-major/', create_major, name='create_major'),
    path('upload-syllabus/', upload_syllabus, name='upload_syllabus'),
    path('create-course/', create_course, name='create_course'),
]