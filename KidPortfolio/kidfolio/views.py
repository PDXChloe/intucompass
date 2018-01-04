from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from kidfolio.models import KidPicPost,Portfolio,Category
from .forms import KidPicForm, PortfolioForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, 'kidfolio/about.html')

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
        return HttpResponseRedirect(reverse('kidfolio:get_portfolios'))
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

def new_portfolio(request):
    form = PortfolioForm(initial={'author': request.user})
    return render(request, 'kidfolio/new_portfolio.html', {'form':form})


def create_portfolio(request):
    if request.method == "POST":
        form = PortfolioForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('kidfolio:get_portfolios'))
        else:
            return HttpResponseRedirect(reverse('kidfolio:new_portfolio'))


def get_kidpost(request, kid_id):
    # return HttpResponse('you are at the detail_view.html') #this url works
    post = get_object_or_404(KidPicPost, pk=kid_id)
    return render(request, 'kidfolio/detail_view.html', {'post': post})



def edit_kidpost(request, kid_id):
    # this not finished
    pass

def new_user(request):
    if request.method == 'POST':
        user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
        login(request, user)
        return HttpResponseRedirect(reverse('kidfolio:get_portfolios'))

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('kidfolio:get_portfolios'))
        else:
            pass
            return HttpResponseRedirect(reverse('kidfolio:index'))

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('kidfolio:index'))

def get_portfolios(request):
    # user = request.user
    #portfolios = user.portfolio_set.all()
    #return render(request, 'kidfolio/portfolios.html', {'portfolios': portfolios})
    return render(request, 'kidfolio/portfolios.html')

def get_this_portfolio(request, portfolio_id):
    portfolio = get_object_or_404(Portfolio, pk=portfolio_id)
    return render(request, 'kidfolio/portfolio_detail.html', {'portfolio': portfolio})

    # want to get all the posts from this particular portfolio and list all portfolio posts in portfolio_detail.html


    # for portfolio in portfolios:
    #     posts = portfolio.kidpicpost_set.all()


