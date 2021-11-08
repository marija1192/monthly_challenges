from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

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
    "december": "Learn Django for 20 minutes!"
}

# Create your views here.

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    forward_month = months[month-1]
    return HttpResponseRedirect("/challenges/" + forward_month)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("Not supported")
        
    