from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from indexview.models import Teacher


# Create your views here.

def index(request):
    teacher = Teacher.objects.get(user = request.user)
    return render(request, 'teacher.html',{'teacher_name': teacher.usertype})