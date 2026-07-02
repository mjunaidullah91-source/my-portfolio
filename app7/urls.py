from django.urls import path
from . import views
app_name = 'contact'
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('project/', views.projects, name='projects'),
    path('blog/', views.blog_view, name='blog'),
    path('blog/<int:blog_id>/', views.blog_detail_view, name='blog_detail'),
    path('contact/', views.contact_view, name='contact'),
    path('skills-education/', views.skills_education_view, name='skills_education'),
    path('navbar/', views.navbar, name='navbar'),
]
