from django.conf.urls import url

from .views import CreatePostView, ListPostView
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    url(r'(?P<subreddit_scope>(.*))/create/?$', csrf_exempt(CreatePostView.as_view()), name='create'),
    url(r'(?P<subreddit_scope>(.*))/list/?$', csrf_exempt(ListPostView.as_view()), name='list'),
]
