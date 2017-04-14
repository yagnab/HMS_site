from django.shortcuts import render
from hms.models import *

def index(request):
    return render(request, 'hms\index.html')

def hotels_list(request):
    hotels = [hotel for hotel in Hotel.objects.all()]
    return render(request, 'hms\hotel_list.html', {'hotels': hotels})
