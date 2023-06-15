from django.core.paginator import Paginator
from django.shortcuts import render
from django.shortcuts import get_object_or_404,redirect, render
from django.db.models import Q
from contact.models import contact

def index(request):
    contacts = contact.objects.all().order_by('-id')

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = { 
        'page_obj': page_obj,
        }

    return render(request, 'contact/index.html', context)

def Contact(request, contact_id):
    single_contact = get_object_or_404(contact, pk=contact_id)
    
    context = {
        'contact': single_contact,
    }

    return render(request, 'contact/contact.html', context)

def search(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('contact:index')
    
    contacts = contact.objects \
        .filter(
            Q(first_name__icontains=search_value) |
            Q(last_name__icontains=search_value) |
            Q(phone__icontains=search_value) |
            Q(email__icontains=search_value) |
            Q(office__icontains=search_value) |
            Q(city__icontains=search_value) 
        )\
        .order_by('-id')
    
    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = { 
        'page_obj': page_obj,
        }

    return render(request, 'contact/index.html', context)
