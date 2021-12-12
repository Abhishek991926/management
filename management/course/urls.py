from django.urls import path
from . import views

urlpatterns = [
    path('org/',views.org_page,name='orglist'),
    path('emp/',views.emp_page,name='emplist'),
]
