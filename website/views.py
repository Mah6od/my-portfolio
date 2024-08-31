from django.shortcuts import render
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
            # messages.success(request, 'Submitted Successfully!')
            messages.add_message(request, messages.SUCCESS, 'Submitted Successfully!')
        else:
            messages.add_message(request, messages.ERROR, 'There is an Error!')
    else:
        form = ContactForm()
        
    return render(request, 'website/contact.html', {'form': form})