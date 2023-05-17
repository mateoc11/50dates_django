from django.shortcuts import render
from django.http import HttpResponse
from .models import users
from datetime import datetime

def portals(request):
    users_list = users.objects.order_by('userid')
    return render(
        request,
        'login/login.html',
        {
            'year': datetime.now().year,
            'users_list': users_list
        }
    )