from django.urls import path
from tasks import views

urlpatterns = [
    path("greet/", views.greeting_),
    path("introduction/", views.introduction_),
    path("time/", views.ddmmyy),
    path("square/", views.square),

]
