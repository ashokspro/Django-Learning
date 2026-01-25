from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        "title" : "Blog-1",
        "author" : "Ak",
        "date_posted" : "25/01/2026",
        "content" : "This is Post 1"
    },
    
     {
        "title" : "Blog-1",
        "author" : "Ak",
        "date_posted" : "25/01/2026",
        "content" : "This is Post 2"
    } 
]



def home(request):
    contexts = {
        "posts" : posts

    }
    return render(request, 'blog/home.html', contexts)
def about(request):
    return render(request, 'blog/about.html', {"title":"Blog-About"})