from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name="create"),
    path('profile', views.profile, name="profile"),
    path('profile_edit', views.profile_edit, name="profile_edit")
]
