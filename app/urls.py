from django.urls import path
from .views import ItemFilterView, ItemDetailView, ItemCreateView, ItemUpdateView, ItemDeleteView
from .views import TrendView, TrendTweetView, TweetUrlView, TrendDetailView


#**************************************************************************************************
# 以下、ひな形
#**************************************************************************************************

urlpatterns = [
    #path('',  ItemFilterView.as_view(), name='index'),                     # 削除
    #path('detail/<int:pk>/', ItemDetailView.as_view(), name='detail'),     # 削除
    path('create/', ItemCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ItemUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ItemDeleteView.as_view(), name='delete'),
    path('',  TrendView.as_view(), name='index'),                       # 追加
    #path('detail/<int:pk>/', TrendDetailView.as_view(), name='detail'),        # 削除
    path('trendtweet/<int:pk>/<str:trendword>/', TrendTweetView.as_view(), name='trendtweet'),
    #path('trendtweet/', TrendTweetView.as_view(), name='trendtweet'),   # 追加　→　削除
    path('tweeturl/', TweetUrlView.as_view(), name='tweeturl'),         # 追加

]
