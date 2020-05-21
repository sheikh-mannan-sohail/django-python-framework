import os
import sys

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    # using f-string response within HttpResponse
    company_name = "Redesign"
    founder = "Ben James"
    return HttpResponse(f"About {company_name}. It is founded by {founder}")


def home(request):
    # using Html
    return HttpResponse("<h1><center> Welcome to Redesign </h1>")


def contact(request):
    # usingfiles
    with open(os.path.join(sys.path[0], 'text_files', 'contact.txt'), 'r') as f:
        return HttpResponse(f.read())


def remove_punctuation(request):
    return HttpResponse("Remove punctuation")


def capitalize_first(request):
    return HttpResponse("Capitalize first")


def space_remover(request):
    return HttpResponse("Space remover")


def char_count(request):
    return HttpResponse("Characters count")
