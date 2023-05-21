def handleUploadedPhoto(f):  
    with open('./static/user_photos/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk) 
    return f'user_photos/{f.name}'

