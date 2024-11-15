from django.shortcuts import render

def index(request):
    return render(request, "index.html")  ## This looks for a folder called "templates" and then searchs for the file name inside it.
