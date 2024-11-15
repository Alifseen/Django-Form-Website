from django.shortcuts import render
from .forms import ApplicationForm

def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["fname"]
            last_name = form.cleaned_data["lname"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]

    return render(request, "index.html")  ## This looks for a folder called "templates" and then searchs for the file name inside it.
