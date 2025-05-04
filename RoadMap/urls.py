from django.urls import path
from django.views.generic import TemplateView
from .views import register, create_major, create_course, upload_syllabus, save_syllabus
from . import api_views

urlpatterns = [
    path('', TemplateView.as_view(template_name='roadmap/home.html'), name='roadmap_home'),
    path('register/', register, name='register'),
    path('create-major/', create_major, name='create_major'),
    path('upload-syllabus/', upload_syllabus, name='upload_syllabus'),
    path('create-course/', create_course, name='create_course'),
    path('save-syllabus/', save_syllabus, name='save_syllabus'),
    
    path('api/getmaps/', api_views.MapListAPIView.as_view(), name='get_maps'),
]