from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse
from django.views.generic.edit import CreateView

from .models import Application


def home_page(request):
    return render_to_response("home_page.html", {})

class ApplicationCreateView(CreateView):
    model = Application
    fields = ['name', 'description', 'work', 'nomination']

    def form_valid(self, form):
        #form.instance.author = self.request.user
        #form.instance.posted = datetime.now()
        form.save()
        return super(ApplicationCreateView, self).form_valid(form)

    def get_success_url(self):
        return "/"
