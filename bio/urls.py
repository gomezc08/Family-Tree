from django.urls import path
from . import views

urlpatterns = [
    #path('person/<int:person_id>/', views.get_member_info, name='member_info'),
    path('<int:PersonID>/', views.get_member_info),
    path('<int:member_id>/', views.get_member_info, name='member_info'),
]
