from django.urls import path

from mysite.blog import views

urlpattern = [
    path('', views.PostView.as_view(), name='home')
]