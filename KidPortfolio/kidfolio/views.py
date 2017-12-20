from django.shortcuts import render
from django.http import HttpResponse
from kidfolio.models import KidPicPost

def index(request):
    kidpost = KidPicPost.objects.all()
    posts = {"kidpost": kidpost}
    print(posts)
    return render(request, 'kidfolio/index.html', context=posts)

# def receive_kidpost(request):
#     my_image = request.FILES['my_image']
#     model = KidPicPost(..., my_image=my_image)
#     KidPicPost.save()