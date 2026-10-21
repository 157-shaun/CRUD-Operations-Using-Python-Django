from django.shortcuts import render,redirect
from crud.models import Students

# Create your views here.
def home(request):
    return render(request,"home.html")

def create(request):
    if  request.method=="POST":
        student_name=request.POST.get("name")
        course_name=request.POST.get("course")
        course_price=request.POST.get("price")
        Students(name=student_name,course=course_name,price=course_price).save()
        
        return render(request,"create.html",{"message":"Course Added Successfully"})
    
    return render(request,"create.html")

def update_list(request):
    students_data=Students.objects.all()
    return render(request,"update_list.html",{"students":students_data})

def update(request,student_id):
    student_data=Students.objects.get(id=student_id)
    if request.method=="POST":
        student_data.name=request.POST.get("name")
        student_data.course=request.POST.get("course")
        student_data.price=request.POST.get("price")
        
        student_data.save()
        return render(request,"update.html",{"student":student_data,"message":"Student Details Updated Successfully"})
    
    
    return render(request,"update.html",{"student": student_data})

def delete(request):
    students=Students.objects.all()
    if request.method=="POST":
        student_id=request.POST.get("student_id")
        Students.objects.get(id=student_id).delete()
        return render(request, {"message":"Data Deleted Successfully"})
    
    return render(request,"delete.html",{"students":students})

def display(request):
    student_data=Students.objects.all()
    return render(request,"display.html",{"students":student_data})
