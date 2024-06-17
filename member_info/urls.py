# member_info/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('member-info/', views.member_info_view, name='member_info'),
    path('form-success/', views.form_success_view, name='form_success'),
]
