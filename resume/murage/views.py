from django.shortcuts import render
from django.core.mail import send_mail
from .forms import MessageForm
from .models import Project

# Create your views here.

def index(request):
    projects = Project.objects.all()
    sent = False
    if request.method == 'POST':
        form = MessageForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            subject = f"Message from {cd['name']}"
            message = f"{cd['message']} by {cd['email']}"
            from_email = f"{cd['email']}"
            send_mail(subject, message, from_email, ['dennismurage97@gmail.com'])
            sent = True
    else:
        form = MessageForm()

    context = {
        'projects': projects,
        'form': form
    }
    return render(request, 'murage/index.html', context)

