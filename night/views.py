from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Review
from .forms import ReviewForm
from .forms import PostForm

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
    if request.method == "POST":
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.author = request.user
            review.post = post
            review.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Review submitted and awaiting approval'
            )

    review_form = ReviewForm()

    return render(
        request,
        "night/post_detail.html",
        {
            "post": post,
            "reviews": reviews,
            "review_count": review_count,
            "review_form": review_form,
        },
    )


def review_edit(request, slug, review_id):
    """
    view to edit reviews
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        review = get_object_or_404(Review, pk=review_id)
        review_form = ReviewForm(data=request.POST, instance=review)

        if review_form.is_valid() and review.author == request.user:
            review = review_form.save(commit=False)
            review.post = post
            review.approved = False
            review.save()
            messages.add_message(request, messages.SUCCESS, 'Review Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating review!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def review_delete(request, slug, review_id):
    """
    view to delete review
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    review = get_object_or_404(Review, pk=review_id)

    if review.author == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'Review deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own reviews!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def add_post(request):
    """
    Display add_post page.

    **Context**

    **Template:**

    :template:`night/add_post.html`
    """

    if request.method == "POST":
        post_form = PostForm(data=request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Post submitted and awaiting approval'
            )

    post_form = PostForm()

    return render(
        request,
        "night/add_post.html",
        {
            "post_form": post_form,
        },
    )


def post_edit(request, post_id):
    """
    view to edit posts
    """
    post = get_object_or_404(Post, pk=post_id)
    post_form = PostForm(instance=post)

    if request.method == "POST":

        post_form = PostForm(data=request.POST, instance=post)

        if post_form.is_valid() and post.author == request.user:
            post = post_form.save(commit=False)
            post.post = post
            post.approved = False
            post.save()
            messages.add_message(request, messages.SUCCESS, 'Post Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating post!')

        return HttpResponseRedirect(reverse('home'))
 
    return render(
        request,
        "night/add_post.html",
        {
            "post_form": post_form,
        },
    )        

def post_delete(request, post_id):
    """
    view to delete post
    """
    post = get_object_or_404(Post, pk=post_id)

    if post.author == request.user:
        post.delete()
        messages.add_message(request, messages.SUCCESS, 'Post deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own post!')

    return HttpResponseRedirect(reverse('home'))
