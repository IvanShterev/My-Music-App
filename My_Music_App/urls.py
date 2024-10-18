
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('My_Music_App.common.urls')),
    path('album/', include('My_Music_App.albums.urls')),
    path('profile/', include('My_Music_App.profiles.urls')),
]
