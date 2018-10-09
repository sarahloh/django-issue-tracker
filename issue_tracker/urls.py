"""issue_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path, include
from accounts import urls as urls_accounts
from home import urls as urls_home
from home.views import index
from django.views import static
from .settings import MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('accounts/', include(urls_accounts)),
    re_path('^media/(?P<path>.*)$', static.serve,
            {'document_root': MEDIA_ROOT}),
]
