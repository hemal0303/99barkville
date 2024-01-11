from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Dog, Breed, Blog
from app.utils import paginatePost


def home(request):
    return render(request, "app/home.html")


def blogs(request):
    blogs = Blog.objects.all().order_by("created_at")
    custom_range, blogs = paginatePost(request, blogs, 9)
    return render(
        request,
        "app/blogs.html",
        {
            "blogs": blogs,
            "custom_range": custom_range,
            "pagesize": 9,
        },
    )


def blog_details(request, id):
    try:
        blog = Blog.objects.get(id=id)
        if blog:
            return render(request, "app/blog_details.html", {"blog": blog})
    except Exception as e:
        return redirect("blogs")


def dogs(request):
    dogs = Dog.objects.all()
    custom_range, dogs = paginatePost(request, dogs, 9)
    return render(
        request,
        "app/dogs.html",
        {
            "dogs": dogs,
            "custom_range": custom_range,
            "pagesize": 9,
        },
    )


def dog_details(request, id):
    try:
        dog = Dog.objects.get(id=id)
        if dog:
            return render(request, "app/dog_details.html", {"dog": dog})
    except Exception as e:
        print("e", e)
        return redirect("dogs")


def donate(request):
    return render(request, "app/donate.html")


def service_details(request):
    return render(request, "app/service_details.html")


def about_us(request):
    return render(request, "app/about_us.html")
