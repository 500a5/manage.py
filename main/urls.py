from . import views
from django.urls import path, include

urlpatterns = (
    path('', views.index, name='news'),
    path('timetable/', views.timetable, name='timetable'),
    path('references/', views.create, name='references'),
    path('<int:pk>/', views.NewsDetailView.as_view(), name='news-detail'),
    path('register', views.RegisterFormView.as_view(), name='register'),
    path('login', views.LoginFormView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
)
