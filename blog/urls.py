from . import views
from django.urls import path, include 

urlpatterns = [
    path('',views.post_list,name='post_list'),
    path('no_disponibles',views.no,name='no'),
    #path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('accounts/', include('django.contrib.auth.urls')),
]