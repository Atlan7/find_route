"""main URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.urls import path, include

from .views import About
from routes.views import FindRoute


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', FindRoute.as_view(), name='find_route'),
    path('about/', About.as_view(), name='about'),
    path('cities/', include(('cities.urls', 'cities'), namespace='cities')),
    path('trains/', include(('trains.urls', 'trains'), namespace='trains')),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
                    path('__debug__/', include(debug_toolbar.urls)),
                ] + urlpatterns
