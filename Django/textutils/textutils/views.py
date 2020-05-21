import os
import sys

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    parameter_json = {
        "company_name": "Redesign",
        "founder": "Ben James",
        "message": "We restructure you unstructured textual data.\n Wanna try, place the text it in textbox"
    }
    return render(request, 'index.html', parameter_json)


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
    print(request.GET.get("user_query_text"), "default")
    return HttpResponse("Remove punctuation")


def capitalize_first(request):
    return HttpResponse("Capitalize first")


def space_remover(request):
    return HttpResponse("Space remover")


def char_count(request):
    return HttpResponse("Characters count")
