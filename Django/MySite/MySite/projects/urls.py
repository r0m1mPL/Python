from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('aboutmyself/', views.aboutmyself, name='aboutmyself'),
    path('contacts/', views.contacts, name='contacts'),
    path('projects/', views.ProjectsView.as_view(), name='project_list'),
    path('projects/<slug:slug>/', views.ProjectDetailView.as_view(), name='project_detail')
]