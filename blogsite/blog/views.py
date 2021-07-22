from django.views import generic
from django.shortcuts import render
from .models import Post, Keyword


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 10


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


def keyword_view(request, keyword):
    selected_keyword = Keyword.objects.filter(id=keyword)[0]
    keyword_posts = Post.objects.filter(keyword=selected_keyword)
    return render(request, "keyword.html", {"keyword_name":selected_keyword, "keyword": keyword, 'keyword_posts': keyword_posts})