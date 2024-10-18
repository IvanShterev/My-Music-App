from django.shortcuts import render, redirect
from My_Music_App.albums.models import Album
from My_Music_App.profiles.forms import UserForm
from My_Music_App.profiles.models import Profile


def index(request):

    profile = Profile.objects.first()
    albums = Album.objects.all()
    context = {
        'profile': profile,
        'albums': albums
    }
    if profile:
        return render(request, 'home/home-with-profile.html', context)

    form = UserForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form
    }

    return render(request, 'home/home-no-profile.html', context)