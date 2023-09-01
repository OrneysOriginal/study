from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Advertisements
from .forms import AdvertisementsForm
from django.urls import reverse, reverse_lazy

def logout_view(request):
    logout(request)
    return redirect(reverse('login'))

def index(request):
    advertisements = Advertisements.objects.all()
    context = {'advertisements': advertisements,'logout': logout_view(request)}
    return render(request, 'app_advertisements/index.html', context)


@login_required(login_url=reverse_lazy('login'))
def advertisement_post(request):
    if request.user.is_authenticated:
        return redirect(reverse('login'))
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
    return render(request, 'app_advertisements/advertisement-post.html', context)


def top_sellers(request):
    context = {'logout': logout_view(request)}
    return render(request, 'app_advertisements/top-sellers.html', context)

def advertisement_detail(request,pk):
    advertisement = Advertisements.objects.get(id=pk)
    context = {
        'advertisement': advertisement
    }
    return render(request, 'app_advertisements/advertisement.html', context)

# Create your views here.
