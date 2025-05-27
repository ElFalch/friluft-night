from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post

# Create your views here.


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
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
    reviews = post.reviews.all().order_by("-created_on")
    review_count = post.reviews.filter(approved=True).count()

    return render(
        request,
        "night/post_detail.html",
        {
            "post": post,
            "reviews": reviews,
            "review_count": review_count,
        },
    )
