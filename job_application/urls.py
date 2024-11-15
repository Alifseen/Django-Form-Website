from django.urls import path
from . import views

## connected "" home page to index html. In flask this was done using @app.route("")
urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]
