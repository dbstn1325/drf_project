
from django.urls import path

# from watchlist_app.views import movie_list, movie_detail
from watchlist_app.api.views import WatchListAV, WatchDetailAV, StreamPlatformAV, StreamPlatformDetailAV

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie_list'), 
    path('<int:pk>/', WatchDetailAV.as_view(), name="movie"),
    path('stream/', StreamPlatformAV.as_view(), name="stream_list"),
    path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name="stream"),
]
