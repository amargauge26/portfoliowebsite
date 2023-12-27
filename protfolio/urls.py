from protfolio import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('blog', views.handleblog, name='handleblog'),
    path('<path:external_url>/', views.external_redirect, name='external_redirect'),

]
