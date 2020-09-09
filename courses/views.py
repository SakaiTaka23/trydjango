from django.shortcuts import render
from django.views import View

from .models import Courses

# Create your views here.


class CourseListView(View):
    template_name = 'courses/course_list.html'
    queryset = Courses.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        context = {'object_list':self.queryset}
        return render(request, self.template_name, context)


def my_fbv(request, *args, **kwargs):
    return render(request, 'about.html', {})
