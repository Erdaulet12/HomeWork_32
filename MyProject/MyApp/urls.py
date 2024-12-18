from django.urls import path
from .views import upload_file_view, file_list_view

urlpatterns = [
    path('upload_file/', upload_file_view, name='upload_file'),
    path('files/', file_list_view, name='file_list'),
]
