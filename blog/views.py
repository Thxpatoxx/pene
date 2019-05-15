from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from .models import Implementodep
from .forms import ImplementodepForm,ImplementodepeditForm

def post_list(request):
    Implementodeps = Implementodep.objects.order_by('implemento')
    return render(request, 'blog/post_list.html', {'Implementodeps': Implementodeps})
def no(request):
    Implementodeps = Implementodep.objects.order_by('implemento')
    return render(request, 'blog/post_list_no.html', {'Implementodeps': Implementodeps})
def post_new(request):
    if request.method == "POST":
        form = ImplementodepForm(request.POST)
        if form.is_valid():
            Implementodep = form.save(commit=False)
            Implementodep.save()
            return redirect('post_list')
    else:
        form = ImplementodepForm()
    return render(request, 'blog/post_edit.html', {'form': form})
def post_edit(request, pk):
    Implementodeps = get_object_or_404(Implementodep, pk=pk)
    if request.method == "POST":
        form = ImplementodepeditForm(request.POST, instance=Implementodeps)
        if form.is_valid():
            Implementodeps = form.save(commit=False)
            Implementodeps.save()
            return redirect('post_list')
    else:
        form = ImplementodepeditForm(instance=Implementodeps)
    return render(request, 'blog/post_edit.html', {'form': form})