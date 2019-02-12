from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse
from .models import TempValues
import json

def index(request):
    return render(request,"index.html",context={})

@csrf_exempt
def get_values(request):
    if request.method=="POST":
        data=json.loads(request.body)
        try:
            temp=data["Temperature"]
            t=TempValues(temperature=str(temp)).save()
        except KeyError:
            pass
        print(data)
        return JsonResponse(data)

@csrf_exempt
def get_latest_temp(request):
    data={}
    t=TempValues.objects.all().last()
    if t:
        data["temperature"]=t.temperature
        data["timestamp"]=t.time.strftime("%m/%d/%Y, %H:%M:%S")
    return JsonResponse(data)
