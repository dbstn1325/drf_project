
from django.urls import path, include

# from watchlist_app.views import movie_list, movie_detail
from watchlist_app.api.views import ReviewCreate, StreamPlatformVS, WatchListAV, WatchDetailAV, StreamPlatformAV, StreamPlatformDetailAV, ReviewList, ReviewDetail
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('list', StreamPlatformVS, basename='streamplatform')


urlpatterns = [
    # path('list/', WatchListAV.as_view(), name='movie_list'), 
    path('<int:pk>/', WatchDetailAV.as_view(), name="movie-all-options"),
    
    path('', include(router.urls)),
    
    # path('stream/', StreamPlatformAV.as_view(), name="stream_list"),
    # path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name="stream"),
    
    # path('review/', ReviewList.as_view(), name="review_list"),
    # path('review/<int:pk>', ReviewDetail.as_view(), name="review_detail"),
    path('<int:pk>/review-create', ReviewCreate.as_view(), name="movie_review_list"),
    path('<int:pk>/review', ReviewList.as_view(), name="movie_review_list"),
    path('review/<int:pk>', ReviewDetail.as_view(), name="movie_review_detail"),
    
    
]
