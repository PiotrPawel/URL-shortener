from django.http import Http404
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import RedirectView

from .models import UserUrl
from .forms import UrlForm


class HomeView(View):
    def get(self, request, *args, **kwargs):
        form = UrlForm()
        context = {"form": form}
        return render(request, 'main/home.html', context)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = UrlForm(request.POST)
            if form.is_valid():
                new_url = form.cleaned_data.get("long_url")
                obj = UserUrl.objects.create(long_url=new_url)
                new_context = {"object": obj}
                return render(request, 'main/success.html', new_context)

            else:
                form = UrlForm()
        form = UrlForm()
        context = {'form': form}
        return render(request, 'main/home.html', context)


def redirect_view(request, short_url):
    try:
        long_url = UserUrl.objects.filter(short_url=short_url)[0]
        return redirect(long_url.long_url)
    except:
        raise Http404('This short URL is not valid!')
    return redirect('/')
