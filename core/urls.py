from django.urls import path
from .views import upload_file, process_excel_api, get_all_records

urlpatterns = [
    path('api/v1/files/upload', upload_file),
    path('api/v1/process-excel', process_excel_api),
    path('api/v1/getAll', get_all_records),
]