from django.shortcuts import render
from django.http import HttpResponse
from .models import Users,Photos
from datetime import datetime
from django.views.decorators.csrf import csrf_protect 
from portals.forms.forms import photoForm
from portals.functions.functions import handleUploadedPhoto
from django.shortcuts import redirect

def portals(request):
    return render(
        request,
        'login/login.html'
    )

@csrf_protect 
def searchPhotos(request):
    password = request.POST['password']
    user_id = Users.objects.get(user_password=password).userid
    return redirect('photos', userid=user_id)

def redirectPhotos(request,userid):
    photos_list = Photos.objects.filter(userid=userid)
    return render(
        request,
        'photos/pictures.html',
        {
            'year': datetime.now().year,
            'photo_data': photos_list
        }
    )

@csrf_protect 
def photoUpload(request):  
    if request.method == 'POST':  
        image_id = request.POST['id']
        userid = request.POST['userid']
        file_url = handleUploadedPhoto(request.FILES['pyPhoto']) 
        photo = Photos.objects.get(userid=userid,image_id=image_id)
        photo.imagepath = file_url
        photo.save()
        return redirect('photos', userid=userid)  