from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("service-details/", views.service_details, name="service_details"),
    path("portfolio-details/", views.portfolio_details, name="portfolio_details"),
    path("starter-page/", views.starter_page, name="starter_page"),
    path("forms/contact/", views.form_ok, name="contact"),
    path("forms/newsletter/", views.form_ok, name="newsletter"),
    path("forms/consultation/", views.form_ok, name="consultation"),
]
