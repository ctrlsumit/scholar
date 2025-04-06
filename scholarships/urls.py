from django.urls import path
from .views import ScholarshipListView

urlpatterns = [
    path('scholarships/', ScholarshipListView.as_view(), 
         name='scholarship_list'),
]
