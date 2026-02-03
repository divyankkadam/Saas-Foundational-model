from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisits

def home_page_view(request, *args , **kwargs):
    return about_view(request, *args, **kwargs)

def about_view(request, *args , **kwargs):
    
    name = "divyank kadam"
    qs = PageVisits.objects.all()
    page_qs = PageVisits.objects.filter(path=request.path)

    try:
        percent = (page_qs.count()*100.0) / qs.count()
    except:
        percent = 0
        
    context = {
        "name": name,
        "page_visit_count": page_qs.count(),
        "percent": percent,
        "total_visit_count":qs.count(),
    }

    path = request.path
    print("path", path)

    PageVisits.objects.create(path=request.path)

    return render(request , "home.html", context)