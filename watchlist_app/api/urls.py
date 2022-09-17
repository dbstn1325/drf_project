
from django.urls import path, include

# from watchlist_app.views import movie_list, movie_detail
from watchlist_app.api.views import ReviewCreate, SearchWatchListGV, StreamPlatformVS, UserReview, WatchListAV, WatchDetailAV, StreamPlatformAV, StreamPlatformDetailAV, ReviewList, ReviewDetail
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('list', StreamPlatformVS, basename='streamplatform')


urlpatterns = [
    # path('list/', WatchListAV.as_view(), name='movie_list'), 
    path('<int:pk>/', WatchDetailAV.as_view(), name="movie-all-options"),
    path('list2/', SearchWatchListGV.as_view(), name="search_watch-list"),
    
    path('', include(router.urls)),

    path('<int:pk>/review-create/', ReviewCreate.as_view(), name="movie_review_list"),
    path('<int:pk>/review/', ReviewList.as_view(), name="movie_review_list"),
    path('review/<int:pk>/', ReviewDetail.as_view(), name="movie_review_detail"),
    
    path('reviews/', UserReview.as_view(), name="user_review"),
    
    
    
    # path('stream/', StreamPlatformAV.as_view(), name="stream_list"),
    # path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name="stream"),
]
