
from django.urls import path
from .views import ImageDetailView
from myapp.views import home,photos,search_profile,addImage

urlpatterns = [
    path('',home, name='home'),
    path('image/<int:pk>/', ImageDetailView.as_view(), name='image_detail'),
    path('photos/', photos, name='photos'),
    path('search_profile/', search_profile, name='search_profile'),
    path('addImage/', addImage, name='addImage'),
    

   
]
