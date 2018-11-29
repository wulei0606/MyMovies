"""MyMovies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path, re_path, include
from django.contrib import admin
from django.conf import settings
from django.views.static import serve

from users.views import IndexView,LoginView,LoginOutView,RegisterView
from movies.views import AnimationView,PlayView
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',IndexView.as_view(),name="index"),
    path('login/',LoginView.as_view(),name="login"),
    path('logout/',LoginOutView.as_view(),name="logout"),
    path('register/',RegisterView.as_view(),name="register"),
    path('animation/',AnimationView.as_view(),name="animation"),
    re_path('play/(?P<id>\d+)/$',PlayView.as_view(),name="play"),
    # re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

    # path('play/')
]
urlpatterns += static('/media/', document_root=settings.MEDIA_ROOT)