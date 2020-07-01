from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    index_data = {
        'navbar_insert': 'Navbar Title - blah!'
    }

    return render(request, 'test_first_app/index.html', context=index_data)


def help_page(request):
    help_data = {
        'navbar_insert': 'Navbar Title - help!'
    }

    return render(request, 'test_first_app/help.html', context=help_data)
