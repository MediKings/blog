from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib.auth import get_user_model


User = get_user_model()


def Home(request):
    users = User.objects.all()
    template_name = 'post/index.html'
    context = {'users': users}
    return render(request, template_name, context)


def Contact(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    template_name = 'post/contact.html'
    context = {}
    return render(request, template_name, context)
