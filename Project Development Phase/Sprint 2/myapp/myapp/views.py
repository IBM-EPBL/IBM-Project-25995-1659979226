from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from newsapi import NewsApiClient
from django.contrib.auth import logout

def register(request):
    return render(request, "register.html")

def login(request):
    return render(request, "login.html")

@login_required
def home(request):
    print(request.user)
    if request.method == "POST":
        newsapi = NewsApiClient(api_key="")
        # articles = newsapi.get_top_headlines(q=request.POST["news"],language="en",country="in")
        articles = newsapi.get_everything(q=request.POST["news"],
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)
        data = {"articles": articles['articles']}
        print(data)
        return render(request, "home.html", data)

    return render(request, "home.html")

@login_required
def logout_user(request):
    logout(request)
    return redirect('/login')