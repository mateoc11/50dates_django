from django.shortcuts import render
from .models import Users,Photos
from datetime import datetime
from django.views.decorators.csrf import csrf_protect 
from portals.functions.functions import handleUploadedPhoto
from django.shortcuts import redirect

def portals(request):
    return render(
        request,
        'login/login.html',
        {'error': ""}
    )

@csrf_protect 
def searchPhotos(request):
    password = request.POST['password']
    try:
        user_id = Users.objects.get(user_password=password).userid
    except:
        return render(
        request,
        'login/login.html',
        {'error': "Contraseña Incorrecta"}
        )
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
        file_url = handleUploadedPhoto(request.FILES[f'myPhoto{image_id}']) 
        photo = Photos.objects.get(userid=userid,image_id=image_id)
        photo.imagepath = file_url
        photo.save()
        return redirect('photos', userid=userid)  