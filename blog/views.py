from django.shortcuts import render
from django.utils import timezone
from .models import Implementodep

def post_list(request):
    Implementodeps = Implementodep.objects.order_by('folio')
    return render(request, 'blog/post_list.html', {'Implementodeps': Implementodeps})
def no(request):
    Implementodeps = Implementodep.objects.order_by('folio')
    return render(request, 'blog/post_list_no.html', {'Implementodeps': Implementodeps})