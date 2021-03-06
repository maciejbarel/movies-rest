"""movies_rest URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from movies.views import MoviesView, MovieView, PeopleView, PersonView, BaseView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^movies/$', MoviesView.as_view()),
    url(r'^movies/(?P<pk>(\d)+)/$', MovieView.as_view()),
    url(r'^people/$', PeopleView.as_view()),
    url(r'^people/(?P<pk>(\d)+)/$', PersonView.as_view(), name='person_detail'),
    url(r'^$', BaseView.as_view(), name='base'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
