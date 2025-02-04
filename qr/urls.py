from django.urls import path
from .views import certificate_form_view, certificate_list_view, download_certificate_pdf

urlpatterns = [
    path('', certificate_form_view, name='certificate_form'),
    path('certificates/', certificate_list_view, name='certificate_list'),
    path('download/<int:pk>/', download_certificate_pdf, name='download_certificate_pdf'),
]
