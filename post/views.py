from django.shortcuts import render


def Home(request):
    template_name = 'post/index.html'
    context = {}
    return render(request, template_name, context)
