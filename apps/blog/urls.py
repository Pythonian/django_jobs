from django.urls import path

from .views import home, post, archive, post_search, category


urlpatterns = [
    path('archive/', archive, name='archive'),
    path('category/<slug:slug>/', category, name='category'),
    #     path('tag/', tag, name='tag'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         post, name='post'),
    path('search/', post_search, name='post_search'),
    path('', home, name='home'),
]

# from django.urls import path
# from . import views
# from .feeds import LatestPostsFeed

# app_name = 'blog'

# urlpatterns = [
#     # Post views
#     path('', views.post_list, name='post_list'),
#     # path('', views.PostListView.as_view(), name='post_list'),
#     path('tag/<slug:tag_slug>/',
#          views.post_list, name='post_list_by_tag'),
#     path('<int:post_id>/share/',
#          views.post_share, name='post_share'),
#     path('<int:post_id>/comment/',
#          views.post_comment, name='post_comment'),
#     path('feed/', LatestPostsFeed(), name='post_feed'),
#     path('search/', views.post_search, name='post_search'),
    # path('create/', views.create, name='create'),
    # path('update/<int:pk>/', views.update, name='update'),
    # path('delete/<int:pk>/', views.delete, name='delete'),
    # path('tags/<slug:tag>/', views.home, name='posts_by_tag'),
    # path('<slug:slug>/', views.detail, name='detail'),
    # path('', views.home, name='post_list'),
    # # path('<int:year>/<int:month>/<int:day>/<slug:slug>/',
    # #      views.detail, name='detail'),
    # path('<int:post_id>/share/', views.post_share, name='post_share'),
    # path('feed/', LatestPostsFeed(), name='post_feed'),
    # # path('search/', post_search, name='post_search'),
# ]
