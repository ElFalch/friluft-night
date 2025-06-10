from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name='home'),
    path("add_post/", views.add_post, name='add_post'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('edit_review/<int:review_id>',
         views.review_edit, name='review_edit'),
    path('delete_review/<int:review_id>',
         views.review_delete, name='review_delete'),
    path('edit_post/<int:post_id>',
         views.post_edit, name='post_edit'),
    path('delete_post/<int:post_id>',
         views.post_delete, name='post_delete'),
]
