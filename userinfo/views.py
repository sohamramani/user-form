from django.shortcuts import render
from django.http import HttpResponse
# from models import ExtraInfo
# Create your views here.

def patient_entry(request):
    return render(request, 'userinfo/extrainfo.html')

def process_patient_entry(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        profile_pic=request.POST['profile_pic']
        phone_number=request.POST['phone_number']
        gender=request.POST['gender']
        country=request.POST['country']
        hobbies=request.POST['hobbies']
        ExtraInfo=ExtraInfo.objects.create(name=name,email=email, profile_pic=profile_pic, phone_number=phone_number, gender=gender, country=country, hobbies=hobbies )
        ExtraInfo.save()

        return HttpResponse("Data successfully inserted!")
    else:
        return HttpResponse("Invalid request method.")
