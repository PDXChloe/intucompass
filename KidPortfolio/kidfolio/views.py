from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from kidfolio.models import KidPicPost,Portfolio,Category
from .forms import KidPicForm


def index(request):
    kidpost = KidPicPost.objects.all()
    posts = {"kidpost": kidpost}
    print(posts)
    return render(request, 'kidfolio/index.html', context=posts)

# def receive_kidpost(request):
#     my_image = request.FILES['my_image']
#     model = KidPicPost(..., my_image=my_image)
#     KidPicPost.save()


def new_kidpost(request):
    form = KidPicForm(initial={'author': request.user})
    return render(request, 'kidfolio/new_kidpost.html', {'form':form})


def publish_new_kidpost(request):
    form = KidPicForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('kidfolio:index'))
    else:
        return HttpResponseRedirect(reverse('kidfolio:new_kidpost'))
    # title = request.POST['title']
    # image = 'images/' + request.POST['image']
    # print(image)
    # caption = request.POST['caption']
    # portfolio = Portfolio.objects.get(pk=request.POST['portfolio'])
    # category = Category.objects.get(pk=request.POST['category'])
    # user = request.user
    #
    # post = KidPicPost(title=title,image=image,caption=caption,author=user,portfolio=portfolio,category=category)
    # post.save()




#construct a KidPicPost
# Populate the KIdPicPost with data posted
# then save
# then redirect