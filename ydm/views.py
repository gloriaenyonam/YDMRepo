from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def gallery(request):
    return render(request, 'gallery.html')

def gallery_microbit_meetup_2022(request):
    return render(request, 'gallery_detailed_pages/microbit_meetup_2022.html')

def founders(request):
    return render(request, 'founders.html')


def contact(request):
    return render(request, 'contact.html')


def honoured(request):
    return render(request, 'honoured.html')

