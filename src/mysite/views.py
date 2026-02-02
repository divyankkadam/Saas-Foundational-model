from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisits

def home_page_view(request, *args , **kwargs):
    name = "divyank kadam"
    qs = PageVisits.objects.all()
    page_qs = PageVisits.objects.filter(path=request.path)

    context = {
        "name": name,
        "page_visit_count": page_qs.count(),
        "percent": (page_qs.count()*100.0) / qs.count(),
        "total_visit_count":qs.count(),
    }

    path = request.path
    print("path", path)

    PageVisits.objects.create(path=request.path)

    return render(request , "home.html", context)