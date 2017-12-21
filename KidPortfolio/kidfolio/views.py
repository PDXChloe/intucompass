from django.shortcuts import render, get_object_or_404
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

def create_portfolio(request):
    pass
    #not in urls yet

def get_kidpost(request, kid_id):
    # return HttpResponse('you are at the detail_view.html') #this url works
    post = get_object_or_404(KidPicPost, pk=kid_id)
    return render(request, 'kidfolio/detail_view.html', {'post': post})



    # kidpost = KidPicPost.objects.[0] #I know this isn't right, I just want one kidpost I clicked on in the index.html
    # return render(request, 'kidfolio/detail_view.html', {'kidpost':kidpost})

def edit_kidpost(request):
    # this not finished
    return HttpResponse('works for me')



#construct a KidPicPost
# Populate the KIdPicPost with data posted
# then save
# then redirect



def get_portfolios(request):
    user = request.user
    #portfolios = user.portfolio_set.all()
    #return render(request, 'kidfolio/portfolios.html', {'portfolios': portfolios})
    return render(request, 'kidfolio/portfolios.html')

    # for portfolio in portfolios:
    #     posts = portfolio.kidpicpost_set.all()


# separate by portfolio