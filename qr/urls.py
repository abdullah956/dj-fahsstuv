from django.urls import path
from .views import certificate_detail2,get_certificate_data2,certificate_list_view2,get_certificate_data,certificate_detail,certificate_form_view, certificate_list_view, download_certificate_pdf,login_view, signup_view, logout_view

urlpatterns = [
    path('form/', certificate_form_view, name='certificate_form'),
    path('certificates/', certificate_list_view, name='certificate_list'),
    path('certificates2/', certificate_list_view2, name='certificate_list2'),
    path('download/<int:pk>/', download_certificate_pdf, name='download_certificate_pdf'),
    path("", login_view, name="login"),
    path("signup/", signup_view, name="signup"),
    path("logout/", logout_view, name="logout"),
    path('certificates/<int:id>/', certificate_detail, name='certificate_detail'),
    path('certificates2/<int:id>/', certificate_detail2, name='certificate_detail2'),
     path('certificate-data/<int:pk>/', get_certificate_data, name="certificate_data"),
          path('certificate-data2/<int:pk>/', get_certificate_data2, name="certificate_data2"),

]
