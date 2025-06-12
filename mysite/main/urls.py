#this is where we define the paths to our webpages

from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>", views.index, name='index'),

]