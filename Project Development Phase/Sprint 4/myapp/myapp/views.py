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
        data = {"articles": articles['articles'], "title" : "News related to %s"%(request.POST["news"])}
        # print(data)
        return render(request, "h.html", data)
    newsapi = NewsApiClient(api_key="6b076c8833b64a37b755b2a42e2d5d7a")
    articles = newsapi.get_top_headlines( category='business',
                                          language='en',
                                          country='us')
    data = {"articles": articles['articles'], "title" : "Headlines"}
    return render(request, "h.html", data)

@login_required
def logout_user(request):
    logout(request)
    return redirect('/login')