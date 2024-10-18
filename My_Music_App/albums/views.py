from django.shortcuts import render, redirect

from My_Music_App.albums.models import Album
from My_Music_App.albums.forms import AlbumForm, EditAlbumForm, DeleteAlbumForm
from My_Music_App.profiles.models import Profile


def add_album(request):
    form = AlbumForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.owner_id = Profile.objects.first().pk
            form.save()
            return redirect('home')

    context = {
        'form': form
    }

    return render(request, 'album/album-add.html', context)


def details_album(request, pk):
    album = Album.objects.get(pk=pk)
    context = {
        'album': album
    }
    return render(request, 'album/album-details.html', context)


def edit_album(request, pk):
    album = Album.objects.get(pk=pk)
    form = EditAlbumForm(instance=album)
    if request.method == 'POST':
        form = EditAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'album': album,
        'form': form,
    }
    return render(request, 'album/album-edit.html', context)


def delete_album(request, pk):
    album = Album.objects.get(pk=pk)
    form = DeleteAlbumForm(instance=album)
    if request.method == 'POST':
        album.delete()
        return redirect('home')

    context = {
        'album': album,
        'form': form,
    }
    return render(request, 'album/album-delete.html', context)




























