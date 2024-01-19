from django.shortcuts import render

# Create your views here.
import datetime

def filters(request):

    dt=datetime.datetime.now()
    d={'data':'East or West HARSHAD sir is Best','dt':dt,'c':4}
    return render(request,'filters.html',d)