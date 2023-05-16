from django.urls import path
from . views import ListBlogs,PostBlog,BlogDetail,BlogDeleteConfirmation,BlogDelete,BlogUpdate

app_name = 'blogs'

urlpatterns = [
    path('',ListBlogs,name="list-blogs"),
    path('create-blog/',PostBlog,name="create-blog"),
    path('blog-detail/<int:pk>',BlogDetail,name="blog-detail"),
    path('blog-update/<int:pk>',BlogUpdate,name="blog-update"),
    path('blog-delete-confirmation/<int:pk>',BlogDeleteConfirmation,name="blog-delete-confirmation"),
    path('blog-delete/<int:pk>',BlogDelete,name="blog-delete"),
]