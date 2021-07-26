from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    names = ["Douglas", "Nikita", "Marcus", "Eric", "Danny", "Donald"]
    context = {
        'names': names,  # keyword == 1st word, value == 2nd word
    }
    return render(request, "home.html", context)