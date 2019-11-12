from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *

# Create your views here.
def home(request):
    
    if request.POST :
        recherche = request.POST.get('rech')
        
        contacts = Contact.objects.all().filter(nom__icontains= recherche).order_by('nom')
    else:
        contacts = Contact.objects.all().order_by('nom')
        paginator = Paginator(contacts, 10)
        page = request.GET.get('page')
    try:
        contact = paginator.get_page(page)
    except EmptyPage:
        contact = paginator(1)
    except PageNotAnInteger:
        contact = paginator(paginator.num_pages)
    return render(request, 'index.html', {'contacts': contact})