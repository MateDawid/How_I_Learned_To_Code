from django.views import generic
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Post, Keyword
from .forms import SearchForm


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 10


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


class KeywordList(generic.ListView):
    queryset = Keyword.objects.order_by('name')
    template_name = 'keyword_list.html'


def keyword_posts_view(request, keyword):
    selected_keyword = Keyword.objects.filter(id=keyword)[0]
    object_list = Post.objects.filter(keyword=selected_keyword).order_by('-created_on')
    paginator = Paginator(object_list, 10)
    page = request.GET.get('page')
    try:
        keyword_posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        keyword_posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        keyword_posts = paginator.page(paginator.num_pages)

    return render(request, "keyword_posts.html", {"keyword_name": selected_keyword, "keyword": keyword, 'keyword_posts': keyword_posts})


def search_form_view(request):
    form = SearchForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            request.session['search_paramethers'] = request.POST
            # return redirect(search_result_view)
    return render(request, "search_form.html", {"form": form})


