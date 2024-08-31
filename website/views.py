from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from website.forms import NameForm, ContactForm
from django.contrib import messages

def index_view(request):
    return render(request, 'index.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Submitted Successfully!')
        else:
            messages.error(request, 'There was an error.')
    else:
        form = ContactForm()
        
    return render(request, 'website/contact.html', {'form': form})