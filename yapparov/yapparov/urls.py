"""yapparov URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from hi import views
from django.urls import path, include

post_patterns = [
    path("",views.post),
    path("last",views.last),
    path("popular",views.popular),
    path("like",views.like),
    path("coment",views.coment),
    path("error",views.error),
]

urlpatterns = [
    path('', views.index),
    path("post/",include(post_patterns)),
    path("post/<int:id>/", include(post_patterns)),
    path("user/",views.user),
    path("about/", views.about),
    path('contacts/',views.contacts),
    path("access/<str:name>/<str:password>",views.access),
    path("access/<str:name>",views.access),
    path("json",views.json),
    path("set",views.set),
    path("get",views.get),
]
