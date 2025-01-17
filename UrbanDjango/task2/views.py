from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

def func_template(request):
    return render(request, 'second_task/func_template.html')

class ClassTemplate(TemplateView):
    template_name = 'second_task/class_template.html'
