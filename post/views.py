from django.shortcuts import render


def Home(request):
    template_name = 'post/index.html'
    context = {}
    return render(request, template_name, context)


def Contact(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    template_name = 'post/contact.html'
    context = {}
    return render(request, template_name, context)
