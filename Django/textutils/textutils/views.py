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
    user_query_text = request.POST.get("user_query_text", "default")
    remove_punc = request.POST.get("remove_punc", "off")
    capitalize = request.POST.get("capitalize", "off")
    remove_newlines = request.POST.get("remove_newlines", "off")
    character_count = request.POST.get("character_count", "off")
    # if checkbox is ticked value  will be on else we set value to off

    structured_text = ""

    if remove_punc == "on":
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        for character in user_query_text:
            if character not in punctuations:
                structured_text = structured_text + character
        params = {"user_input_text": user_query_text, "cleaned_text": structured_text}
        return render(request, "removed_punctuation_response.html", params)
    elif capitalize == "on":
        structured_text = user_query_text.upper()
        params = {"user_input_text": user_query_text, "cleaned_text": structured_text}
        return render(request, "removed_punctuation_response.html", params)
    elif remove_newlines == "on":
        structured_text = "".join(filter(lambda char: char is not '\n', user_query_text))
        params = {"user_input_text": user_query_text, "cleaned_text": structured_text}
        return render(request, "removed_punctuation_response.html", params)

    elif character_count == "on":
        structured_text = len(user_query_text)
        params = {"user_input_text": user_query_text, "cleaned_text": structured_text}
        return render(request, "removed_punctuation_response.html", params)
    return HttpResponse("Please select the  switch-box to perform  analysis")


def capitalize_first(request):
    return HttpResponse("Capitalize first")


def space_remover(request):
    return HttpResponse("Space remover")


def char_count(request):
    return HttpResponse("Characters count")
