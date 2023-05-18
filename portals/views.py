from django.shortcuts import render
from django.http import HttpResponse
from .models import Users,Photos
from datetime import datetime
from django.views.decorators.csrf import csrf_protect 

def portals(request):
    users_list = Users.objects.order_by('userid')
    return render(
        request,
        'login/login.html',
        {
            'year': datetime.now().year,
            'users_list': users_list
        }
    )

@csrf_protect 
def searchPhotos(request):
    password = request.POST['password']
    photos_list = Photos.objects.filter(userid=Users.objects.get(user_password=password).userid)
    return render(
        request,
        'photos/pictures.html',
        {
            'year': datetime.now().year,
            'photo_data': photos_list
        }
    )