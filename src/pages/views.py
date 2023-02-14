from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def homepage_view(request, *args, **kwargs):
    #We cannot just return a string, but a HTTP request with that string
    print(args, kwargs)
    print(request)
   # return HttpResponse("<h1> Hello World </h1>") #string of HTML code
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    #return HttpResponse("<h1> Contact view </h1>") #string of HTML code
    return render(request, "contact.html", {})


def about_view(request, *args, **kwargs):
    #return HttpResponse("<h1> Contact view </h1>") #string of HTML code
    #We can create a dictionary which contains the context that we then send to the template
    listnumbers = []
    for i in range(0, 10):
        listnumbers.append(i)
    my_context = {
        "abc": 312,
        "my_number": 123,
        "my_list": [123, 456, 789, "abc"],
        "my_numbers": listnumbers,
        "title": "About Hello world",
        "my_html": "<h1>Hello World</h1>",
    }
    return render(request, "about.html", my_context)


def social_view(request, *args, **kwargs):
    #return HttpResponse("<h1> Contact view </h1>") #string of HTML code
    return render(request, "social.html", {})
