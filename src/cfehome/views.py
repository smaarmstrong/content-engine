from django.http import HttpResponse

def home_pag(request):
    return HttpResponse("Hello World")