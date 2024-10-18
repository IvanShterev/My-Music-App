from django import forms
from My_Music_App.albums.models import Album


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['album_name', 'artists', 'genre', 'description', 'image_url', 'price']
        widgets = {
            'album_name': forms.TextInput(attrs={'placeholder': 'Album Name'}),
            'artists': forms.TextInput(attrs={'placeholder': 'Artists'}),
            'genre': forms.Select(choices=Album.CHOICES, attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Image URL'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Price'}),
        }


class EditAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['album_name', 'artists', 'genre', 'description', 'image_url', 'price']


class DeleteAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['album_name', 'artists', 'genre', 'description', 'image_url', 'price']

    def __init__(self, *args, **kwargs):
        super(DeleteAlbumForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['readonly'] = True
            field.widget.attrs['disabled'] = True












