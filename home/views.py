from django.views.generic import TemplateView
from home.forms import HomeForm
from django.shortcuts import render, redirect
from . models import Post, Friend
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
# def home(request):
#     return HttpResponse('It works')

class HomeView(LoginRequiredMixin,TemplateView):
    template_name = 'home/home.html'
    def get(self, request):
        form = HomeForm()
        posts = Post.objects.all().order_by('-created')
        #users = User.objects.all()
        users = User.objects.exclude(id=request.user.id)
        # get my friends make sure u have instance of friends
        try:
            friend = Friend.objects.get(current_user=request.user)
            friends = friend.users.all()
        except Friend.DoesNotExist:
            friends = 'You have not made friends yet'

        #print(posts) # checks wether it is working
        args = {'form': form,
                'posts': posts,
                'users': users,
                'friends': friends}
        return render(request, self.template_name, args)

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            return redirect('home:home')

@login_required
def change_friends(request, operation, pk):
    # logic in home.models
    friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, friend)
    else:
        operation == 'remove'
        Friend.lose_friend(request.user, friend)
    return redirect('home:home')