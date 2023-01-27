from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"), # <- new route
    path('whales/', views.WhaleList.as_view(), name="whales_list"),
    path('whales/new/', views.WhaleCreate.as_view(), name="whales_create"),
    path('whales/<int:pk>/', views.WhaleDetail.as_view(), name="whale_detail"),
    path('whales/<int:pk>/update',views.WhaleUpdate.as_view(), name="whale_update"),
    path('whales/<int:pk>/delete',views.WhaleDelete.as_view(), name="whale_delete"),
]
