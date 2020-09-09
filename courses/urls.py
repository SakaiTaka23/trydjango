from django.urls import path
from .views import (
    my_fbv,
    CourseListView
)

app_name = 'courses'
urlpatterns = [
    path('', CourseListView.as_view(), name='courses-list'),
    path('', my_fbv, name='courses-list'),
]
