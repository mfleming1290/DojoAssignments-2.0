from django.shortcuts import render, redirect
from .models import Course
# Create your views here.
def index(request):
    context = {
    'courses': Course.objects.all()
    }
    return render(request, 'course/index.html', context)

def new(request):
    Course.objects.create(name=request.POST['name'], description=request.POST['description'])
    return redirect('/')

def destroy(request, id):
    context = {
    'id': id,
    'course': Course.objects.get(id=id)
    }
    return render(request, 'course/destroy.html', context)

def delete(request, id):
    context = {
    'id': id
    }
    course = Course.objects.get(id=id)
    course.delete()
    return redirect('/')
