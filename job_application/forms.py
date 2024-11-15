from django import forms


class ApplicationForm(forms.Form):
    fname = forms.CharField(max_length=80)
    lname = forms.CharField(max_length=80)
    email = forms.EmailField()
    date = forms.DateField()
    occupation = forms.CharField(max_length=80)