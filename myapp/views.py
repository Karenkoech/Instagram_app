from multiprocessing import context
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime

from .models import Image,Profile

# Create your views here.
@login_required
def home(request):
    image = Image.objects.all()
    context={
        'image': image
    }
    return render(request, 'myapp/home.html',context)
    


class ImageDetailView(DetailView):
    model = Image
    
 
def photos(request):
    if request.method == 'GET':
        images = Image.objects.all()
        return render(request, 'myapp/photos.html',{'images':images})
    else:
        return render(request, 'myapp/photos.html')

def image_detail(request,pk):
    if request.method == 'GET':
        image = Image.objects.get(id=pk)
        return render(request, 'myapp/image_detail.html',{'image':image})
    else:
        return render(request, 'myapp/image_detail.html')  
   
def search_profile(request):
    if request.method == 'POST':
        image_profile = request.POST['image_profile']
        images = Image.objects.filter(image_profile__profile_bio__icontains=image_profile)
        return render(request, 'myapp/search.html',{'images':images})
    else:
        return render(request, 'myapp/search.html')

@login_required
def addImage(request):
    profiles = Profile.objects.all()

    if request.method == 'POST':
        data=request.POST
        image = request.FILES.get('image')
        return redirect('/photos', data=data, image=image)
    else:
        return render(request, 'myapp/add_post.html',{'profiles':profiles})


        
        


        return render(request, 'myapp/add_post.html')

    