from django.shortcuts import render, redirect
from .models import Student

# Create your views here.

def home(request):
    std = Student.objects.all()
    return render(request, 'std/home.html',{'std':std})

def std_add(request):
    if request.method == "POST":
        print("added")
        stds_regno = request.POST.get("std_regno")
        stds_name = request.POST.get("std_name")
        stds_email = request.POST.get("std_email")
        stds_phone = request.POST.get("std_phone")

        s = Student()
        s.regno = stds_regno
        s.name = stds_name
        s.email = stds_email
        s.phone = stds_phone
        s.save()
        return redirect("/std/home")

    return render(request, 'std/add_std.html')

def delete_std(request, regno):
    s = Student.objects.get(pk=regno)
    s.delete()

    return redirect("/std/home")

def update_std(request, regno):
    std = Student.objects.get(pk=regno)
    return render(request, "std/update_std.html",{'std':std})

def do_update_std(request, regno):
    stds_regno = request.POST.get("std_regno")
    stds_name = request.POST.get("std_name")
    stds_email = request.POST.get("std_email")
    stds_phone = request.POST.get("std_phone")

    std = Student.objects.get(pk=regno)
    std.regno = stds_regno
    std.name = stds_name
    std.email = stds_email
    std.phone = stds_phone

    std.save()

    return redirect("/std/home")