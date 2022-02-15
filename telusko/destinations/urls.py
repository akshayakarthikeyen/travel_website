from django.urls import path
from .import views

urlpatterns =[
   path('Hyderabad',views.Hyderabad , name = "Hyderabad"),
   path("Pune" , views.Pune ,  name='pune'),
   path("Banglore" , views.Banglore, name = 'Banglore'),
   path("Mumbai" , views.Mumbai, name = 'Mumbai'),
   path("booking" , views.booking , name= "booking")
   
]
