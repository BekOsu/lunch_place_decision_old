from .views import VoteCreateView, MenuListView
from django.urls import path

urlpatterns = [
    path('vote-create/', VoteCreateView.as_view(), name='vote_create'),
    path('voted-list/', MenuListView.as_view(), name='vote_create'),
]
