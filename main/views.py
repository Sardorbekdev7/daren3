from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
# Create your views here.


def contact(request):
    form = ContactForm()
    print('work')
    if request.method == 'POST':
        print(request.POST)
        print(form)
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('.')

    ctx = {
        'form': form
    }
    return render(request, 'main/contact.html', ctx)
