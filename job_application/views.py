from django.shortcuts import render
from .forms import ApplicationForm
from .models import Forms
from django.contrib import messages
from django.core.mail import EmailMessage

def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["fname"]
            last_name = form.cleaned_data["lname"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]

            ## Import the database model and set form values to column names
            Forms.objects.create(fname=first_name,lname=last_name,email=email,date=date,occupation=occupation)

            ## Send email
            body_text = f"""\
            This is just a confirmation:
            Your Submission Details are:
            {first_name}
            {last_name}
            {email}
            {occupation}
            {date}\
            """

            email = EmailMessage("Form Submitted", body_text, to=[email])

            email.send()

            ## Display message on success
            messages.success(request,f"Form Submitted Successfully, Thank you {first_name}")

    return render(request, "index.html")  ## This looks for a folder called "templates" and then searchs for the file name inside it.

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")