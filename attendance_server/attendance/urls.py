from django.urls import path
from .views import register_attendance, download_attendance_records

urlpatterns = [
    path('register/', register_attendance, name='register_attendance'),
    path('download/', download_attendance_records, name='download_attendance_records'),
]
