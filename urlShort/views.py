from django.shortcuts import render, HttpResponse, redirect
from .models import urlModel
import random
import requests
import json

# Create your views here.

def home(request):
    return render(request, "index.html")


def makeshorturl(request):

    if request.method == "POST":
        longurl = request.POST['longurl']

        
        # url = "https://api.short.io/links"

        
        # payload = json.dumps({"hideReferer":False,"httpsLinks":False,"hostname":"http://439z.short.gy/","linkType":"random"})
        # headers = {
        #     'accept': "application/json",
        #     'content-type': "application/json",
        #     'authorization': "pk_lcXtRgddVq4KbJw8"
        #     }

        # response = requests.request("POST", url, data=payload, headers=headers)

        # print(response.text)


        # shorturl = response["shortURL"]
        s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
        shorturl = ("".join(random.sample(s, 5)))
        obj = urlModel.objects.create(longurl=longurl, shorturl=shorturl)
        shorturl = "http://127.0.0.1:8000/" + shorturl
        keys = {"shorturl": shorturl, "longurl": longurl}
    return render(request, "shortener.html", keys)


def redirecturl(request, shorturl):
    try:
        obj = urlModel.objects.get(shorturl=shorturl)
    except urlModel.DoesNotExist:
        obj = None
    if obj is not None:
        obj.count += 1
        obj.save()
        return redirect(obj.longurl)
    else:
        return HttpResponse("Check your Url")
