from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse


def home_page(request):
    return render_to_response("home_page.html", {})
