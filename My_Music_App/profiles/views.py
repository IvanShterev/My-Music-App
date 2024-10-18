from django.shortcuts import render, redirect
from My_Music_App.albums.models import Album
from My_Music_App.profiles.forms import UserDeleteForm
from My_Music_App.profiles.models import Profile


def profile_details(request):
    profile = Profile.objects.first()
    albums = Album.objects.filter(owner=profile.id).count()
    context = {
        'profile': profile,
        'albums': albums
    }
    return render(request, 'profile/profile-details.html', context)


def profile_delete(request):
    profile = Profile.objects.first()
    form = UserDeleteForm(instance=profile)
    if request.method == 'POST':
        profile.delete()
        return redirect('home')

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, 'profile/profile-delete.html', context)