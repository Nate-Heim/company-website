# pages/urls.py

from django.urls import path

from .views import home_page_view, AboutPageView  # new

urlpatterns = [
    path(
        "about/",
        AboutPageView.as_view(),
        name="about",
    ),  # new
    path("", home_page_view, name="home"),
]
