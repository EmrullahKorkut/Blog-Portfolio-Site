from django.urls import path

from blog import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('blog', views.blog, name='blog'),
    path('blog/<slug:slug>',views.blog_details, name='blog_details'),
    path('category/<slug:slug>', views.blog_category, name='blog_category'),
    path('search', views.search, name="search"),
]
