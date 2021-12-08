from django.urls import path
from . import views

urlpatterns = [
    path('org/',views.org_page),
    path('emp/',views.emp_page),
]
