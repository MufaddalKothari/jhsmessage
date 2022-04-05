"""jhsmessage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from demo import views as demoviews
from profileapp import views as paviews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',demoviews.home_view, name='home'),
    path('login/',demoviews.login_view, name='login'),
    path('signup/',demoviews.signup_view, name='signup'),
    path('logout/',demoviews.logout_view, name='logout'),
    path('profile/<str:email>',paviews.profile_view, name='profile'),
    path('profile/newpost/<str:email>',paviews.newpost_view, name='newpost'),
    path('profile/feed/<str:email>',paviews.feed_view, name='test'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
