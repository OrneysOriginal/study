from django.shortcuts import render, redirect
from .models import Advertisements
from .forms import AdvertisementsForm
from django.urls import reverse


def index(request):
    advertisements = Advertisements.objects.all()
    context = {'advertisements': advertisements}
    return render(request, 'index.html', context)


def advertisement_post(request):
    if request.method == "POST":
        form = AdvertisementsForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = Advertisements(**form.cleaned_data)
            advertisement.user = request.user
            advertisement.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = AdvertisementsForm()
    context = {'form': form}
    return render(request, 'advertisement-post.html', context)


def top_sellers(request):
    return render(request, 'top-sellers.html')

# Create your views here.
