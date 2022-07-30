from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm


def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = ContactForm()
    return render(request, 'home.html', {'form': form})
    
def detail(request):
    return HttpResponse("Testing page")