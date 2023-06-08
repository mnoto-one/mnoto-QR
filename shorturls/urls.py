from django.urls import path
from . import views

app_name = 'short_urls'

urlpatterns = [
    path('short-urls/', views.shorten_url, name='shorten'),
    path('short-urls/<str:short_code>/', views.redirect_to_long_url, name='redirect'),
]