from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
# Create your views here.


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        print(request.POST)
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('.')

    ctx = {
        'form': form
    }
    return render(request, 'main/contact.html', ctx)
