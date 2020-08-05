from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# post = [
#     {
#         "author" : "Baksman",
#          "title" : "Blog post 1",
#          "content" : "First blog post on django",
#          "date" : "August 2018"
#     },
#        {
#         "author" : "Ibrahim",
#          "title" : "Blog post 2",
#          "content" : "Second blog post on django",
#          "date" : "August 2020"
#     }
# ]

def home(request):
    context = {
        "posts" : Post.objects.all()
    }
    return render(request,"blog/home.html", context)

def about(request):
    return render(request,"blog/about.html",{"title":"about"})



