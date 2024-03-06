from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.template.loader import render_to_string
from django.urls import reverse

# Create your views here.

# Create monthly challenge dictionary
monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Learn Django for at least 20 minutes every day!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": None
}

months = list(monthly_challenges.keys())


def index(request):
    #list_items = ""

    #Previously it was loop through the dictionary from below code:
    # for month in months:
    #     #month_path = reverse("month_challenge", args=[month])  # challenges/month
    #     list_items += f"<li><a href=\"{month}\">{month.capitalize()}</a></li>"
    #
    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)

    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge_by_number(request, month):
    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid month</h1>")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])  # /challenges/any month
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
        return render(request, "challenges/challenge.html", {
            "text": challenge_text, "month": month
        })
    except:
        raise Http404() #Need to set DEBUG=False for this to work in settings
