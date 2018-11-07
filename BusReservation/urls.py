"""BusReservation URL Configuration

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
from django.views.generic import TemplateView, RedirectView
from django.urls import path


from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', TemplateView.as_view(template_name="Home.html")),
    path('home/', TemplateView.as_view(template_name="Menu.html")),

    path('register/', views.Register),
    path('registerdetails/', views.Registerdetails),

    path('login/', views.login),
    path('logindetails/', views.logindetails),

    path('searchabhi/', views.searchabhi),
    path('searchprasad/', views.searchprasad),
    path('searchbabu/', views.searchbabu),
    path('searchjagan/', views.searchjagan),
    path('searchtown/', views.searchtown),
    #path('searchdrop/', views.searchdrop),
    path('pay/', views.pay),
    path('paydetails/', views.paydetails),

    path('abhi/', TemplateView.as_view(template_name="Abhi.html")),
    path('prasad/', TemplateView.as_view(template_name="Prasad.html")),
    path('babu/', TemplateView.as_view(template_name="Babu.html")),
    path('jagan/', TemplateView.as_view(template_name="Jagan.html")),

    path('upper/', views.upper),
    path('lower/', views.lower),
    path('gents/', views.gentsseats),
    path('ladies/', views.ladiesseats),




]
