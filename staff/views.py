from django.shortcuts import render
from indexview.models import Staff
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    try:
        staff = Staff.objects.get(user = request.user)
    except:
        staff = request.user
        staff.usertype = "Staff"

    return render(request, 'staff.html',{'staff': staff.usertype})

def register_staff(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    confirm_password = request.POST.get('confirm_password')
    staffuser = User.objects.create_user(first_name = first_name, last_name = last_name, username = username, email = email, password = password)
    staff = Staff(user = staffuser)
    staff.save()
    return index(request)



def staff_registration(request):
    return render(request, 'register_staff.html')