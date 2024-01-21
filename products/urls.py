from django.urls import path
from . import views  # the . means in the current folder

# /products/1/detail
urlpatterns = [
    path('', views.index),
    path('new', views.new),
    path('offers', views.offers)
]


# passing a reference to the function since django will call the function for us when a user
#  clicks the link
