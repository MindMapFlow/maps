from django.urls import path
from . import views
from .views import theory_view

urlpatterns = [
    path('', views.index, name='index'),
    path('archive-tests/', views.archive_tests, name='archive_tests'),
    path('archive-material/', views.archive_material, name='archive_material'),
    path('auth/', views.authorization, name='authorization'),
    path('register/', views.registration, name='registration'),
    path('tests/', views.main_test, name='main_test'),
    path('achievements/', views.theory_view, name='theory_view'),  # должно вести на theory_view
path('material/', views.theory_view, name='main_material'),  # если хочешь использовать имя main_material

]


