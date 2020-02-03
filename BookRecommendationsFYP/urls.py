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
from django.contrib import admin
import Test_App.views as test_app

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'', test_app.AllBooks.as_view()),
    re_path(r'(?P<pk>\d+)', test_app.BooksView.as_view()),
    path(r'', test_app.AllAuthor.as_view()),
    re_path(r'(?P<pk>\d+)', test_app.AuthorView.as_view()),
    path('', include('frontend.urls'))

]
