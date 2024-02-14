from django.urls import path
from principal import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.HomeView, name='home'),
    path('recepted/', views.TablaAd, name='recepted'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('contact/', views.ContactView, name='contact'),
    path('login/', views.login_user, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]