from django.shortcuts import redirect, render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect, response
from django.urls import reverse

monthly_challenges = {
    "january":"Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march":"Learn Django for 20 minutes!",
    "april": "Learn Django for 20 minutes!",
    "may": "Learn Django for 20 minutes!",
    "june": "Learn Django for 20 minutes!",
    "july": "Learn Django for 20 minutes!",
    "august": "Learn Django for 20 minutes!",
    "september": "Learn Django for 20 minutes!",
    "october": "Learn Django for 20 minutes!",
    "november": "Learn Django for 20 minutes!",
    "december": None
}

# Create your views here.

def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenge/january
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request ,"challenges/challenge.html", {
            "text": challenge_text,
            "month": month,
        })
    except:
        raise Http404()
        
    