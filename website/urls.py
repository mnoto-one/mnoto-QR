from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('generate-qr/', views.generate_qr_with_logo, name='generate_qr'),
    path('qr-code-generated/', views.qr_code_generated, name='qr_code_generated'),
]