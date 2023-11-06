from . import views
from .views import *
from django.urls import path

urlpatterns = [
    path('register/', RegistrateUser.as_view(), name='register'),
    path('', views.ApplicationsView.as_view(), name='index'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('Applications/create/', views.ApplicationsCreate.as_view(), name='Applications-create'),
    path('Applications/<int:pk>/delete/', views.ApplicationsDelete.as_view(), name='Applications-delete'),
    path('applications/', views.applicationByUserListView.as_view(), name='applicationByUserListView'),
    path('Applications/admin', views.applicationByAdminListView.as_view(), name='applicationByAdminListView'),
    path('Applications/<int:pk>/update/', views.ApplicationsUpdate.as_view(), name='ApplicationsUpdate'),
    path('Applications/createCategory/', views.createCategory.as_view(), name='Category-create'),

]
