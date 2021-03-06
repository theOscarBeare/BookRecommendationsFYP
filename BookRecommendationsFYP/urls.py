"""BookRecommendationsFYP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from . import view
import DataCall.views as DataCall
import Recommendations.views as recomemndations


urlpatterns = [
    url(r'^', view.FrontendAppView.as_view()),
    path('', include('frontend.urls')),
    path(r'admin/', admin.site.urls),
    path(r'', DataCall.AllAuthor.as_view(), name='AllAuthor'),
    re_path(r'(?P<pk>\d+)', DataCall.AuthorView.as_view()),
    path(r'', recomemndations.Allenduser.as_view(), name='Allenduser'),
    re_path(r'(?P<pk>\d+)', recomemndations.enduserView.as_view()),
    path(r'', DataCall.AllBooks.as_view()),
    re_path(r'(?P<pk>\d+)', DataCall.BooksView.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
