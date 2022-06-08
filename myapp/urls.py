
from django.urls import path
from .views import ImageListView,ImageDetailView
from . import views

urlpatterns = [
    path('', ImageListView.as_view(), name='home'),
    path('image/<int:pk>/', ImageDetailView.as_view(), name='image_detail'),
    path('photos/', views.photos, name='photos'),
    path('search_profile/', views.search_profile, name='search_profile'),
    path('addImage/', views.addImage, name='addImage'),
    

   
]
