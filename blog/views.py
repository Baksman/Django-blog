from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from django.contrib.auth.models  import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

# post = [
#     {
#         "author" : "Baksman",
#          "title" : "Blog post 1",
#          "content" : "First blog post on django",
#          "date" : "August 2018"
#     },
#        {
#         "author" : "Ibrahim",
#          "title" : "Blog post 2",
#          "content" : "Second blog post on django",
#          "date" : "August 2020"
#     }


class PostListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]
    paginate_by = 3

class UserPostListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = "blog/user_posts.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get("username"))
        return Post.objects.filter(author= user).order_by("-date_posted")


class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ["title","content"]

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ["title","content"]

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    


@login_required
def about(request):
    return render(request,"blog/about.html",{"title":"about"})



