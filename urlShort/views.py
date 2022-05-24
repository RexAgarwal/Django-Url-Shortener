from ipaddress import ip_address
from django.shortcuts import render, HttpResponse, redirect
from .models import Url_Model, url_analytics, urlModel
import random
import requests
import json
import geocoder
from datetime import datetime



def get_geolocation(ip):
    # ip = requests.get('https://api.ipify.org').content.decode('utf8')
    g = GeoIP2('/home/himanshu/Django-Url-Shortener/urlShort/geoip')
    # location = g.country(ip)
    loc = g.city("5.32.57.218")
    print(loc)
    return loc


def home(request):
    return render(request, "index.html")




def visitor_ip_address(request): 
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR') 
    if x_forwarded_for: 
        ip = x_forwarded_for.split(',')[0] 
        print(ip)
    else: 
        ip = request.META.get('REMOTE_ADDR') 
    return ip
    
    
    
    

def makeshorturl(request):

    if request.method == "POST":
        longurl = request.POST['longurl']
        # campaign_id = request.POST['campaign_id']
        # dlr_id = request.POST['dlr_id']

        s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
        shorturl = ("".join(random.sample(s, 5)))
        
        shorturl = "http://127.0.0.1:8000/" + shorturl
        keys = {"shorturl": shorturl, "longurl": longurl}
        
        # json_data = json.loads(str(request))
        # print(request.META)
        obj = Url_Model.objects.create(longurl=longurl, shorturl=shorturl)
        obj.save()
        return render(request, "shortener.html", keys)
    
    return render(request, "shortener.html")
        
       


    


def redirecturl(request, shorturl):
    print(shorturl)
    try:
        obj = Url_Model.objects.get(shorturl="http://127.0.0.1:8000/"+shorturl)
        print(obj)
    except urlModel.DoesNotExist:
        obj = None
    if obj is not None:
        ip= visitor_ip_address(request)
        location = get_geolocation(ip)
        new_obj = url_analytics.objects.create(date= datetime.now(),ip_address=ip,location=location,url=obj)
        new_obj.save()
        new_obj.count += 1
        new_obj.save()
        return redirect(obj.longurl)
    else:
        return HttpResponse("Check your Url")
