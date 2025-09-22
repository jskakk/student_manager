from django.urls import path
from . import views

app_name = 'student_manager'

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('<int:student_id>/', views.student_detail, name='student_detail'),
]
