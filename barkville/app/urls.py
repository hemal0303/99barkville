from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("blogs/", views.blogs, name="blogs"),
    path("blog_details/<int:id>/", views.blog_details, name="blog_details"),
    path("dogs/", views.dogs, name="dogs"),
    path("dog_details/<int:id>/", views.dog_details, name="dog_details"),
    path("donate/", views.donate, name="donate"),
    path("service_details/", views.service_details, name="service_details"),
    path("about_us/", views.about_us, name="about_us"),
]
