from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post

# Create your views here.


class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = "night/index.html"
    paginate_by = 6

def post_detail(request, slug):
    """
    Display an individual :model:`night.Post`.

    **Context**

    ``post``
        An instance of :model:`night.Post`.

    **Template:**

    :template:`night/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "night/post_detail.html",
        {"post": post},
    )