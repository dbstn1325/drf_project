from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, mixins, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response
from rest_framework.throttling import (AnonRateThrottle, ScopedRateThrottle,
                                       UserRateThrottle)
from rest_framework.views import APIView
from watchlist_app.api.pagination import (WatchlistCuPagination,
                                          WatchlistOPPagination,
                                          WatchlistPagination)
from watchlist_app.api.permissions import (IsAdminOrReadOnly,
                                           IsReviewUserOrReadOnly)
from watchlist_app.api.serializers import (ReviewSerializer,
                                           StreamPlatformSerializer,
                                           WatchListSerializer)
from watchlist_app.api.throttling import (ReviewDetailThrottle,
                                          ReviewListThrottle)
from watchlist_app.models import Review, StreamPlatform, WatchList


class UserReview(generics.ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [ReviewListThrottle, AnonRateThrottle]
    

    def get_queryset(self):
        # username = self.kwargs['username']
        username = self.request.query_params.get('username')
        return Review.objects.filter(review_user__username=username)


# 리뷰 생성
class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Review.objects.all()
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        watchlist = WatchList.objects.get(pk=pk)
        
        # 유저 리뷰생성 중복 처리
        user = self.request.user
        review_queryset = Review.objects.filter(watchlist=watchlist, review_user=user)
        
        if review_queryset.exists():
            raise ValidationError("이미 해당 영화에 리뷰를 남기셨습니다.")
        
        # 리뷰 평균 field 처리
        # 최초
        if watchlist.number_rating == 0:
            watchlist.avg_rating = serializer.validated_data['rating']
        # 후
        else:
            watchlist.avg_rating = ( watchlist.avg_rating + serializer.validated_data['rating'] ) / 2
        
        # 조회 수 처리
        watchlist.number_rating = watchlist.number_rating + 1
        watchlist.save()
        serializer.save(watchlist=watchlist, review_user=user)
        
        
        
# 리뷰 리스트 확인
class ReviewList(generics.ListCreateAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [ReviewListThrottle, AnonRateThrottle]
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)
    

# 리뷰 상세 확인 (업데이트, 삭제)
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewUserOrReadOnly]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'review_detail'


# viewsets => CREATE, UPDATE, DELETE 다 가능!
class StreamPlatformVS(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer



class StreamPlatformAV(APIView):
    permission_classes = [IsAdminOrReadOnly]
    
    def get(self, request):
        platform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platform, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StreamPlatformDetailAV(APIView):
    permission_classes = [IsAdminOrReadOnly]
    
    def get(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'error': 'Not Found'},status=status.HTTP_404_NOT_FOUND)
        platform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(platform)
        return Response(serializer.data)
    
    def put(self, request, pk):
        platform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(platform, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        platform = StreamPlatform.objects.get(pk=pk)
        platform.delete()
        return Response(status.HTTP_204_NO_CONTENT)
        
            

class SearchWatchListGV(generics.ListAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer
    pagination_class = WatchlistPagination
    
    # filter_backends = [filters.SearchFilter]
    # filter_backends = ['title', 'platform__name']
    
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['title', 'active']
    
    # filter_backends = [filters.OrderingFilter]
    # ordering_fields = ['-avg_rating']
    
    
    
    
    

class WatchListAV(APIView):
    permission_classes = [IsAdminOrReadOnly]
    
    def get(self, request):
        watchList = WatchList.objects.all()
        serializer = WatchListSerializer(watchList, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        # validated_data에 딱맞게 들어왔다면,
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
    
        
class WatchDetailAV(APIView):
    permission_classes = [IsAdminOrReadOnly]
    throttle_classes = [AnonRateThrottle]
    
    def get(self, request, pk):
        try:
            watchList = WatchList.objects.get(pk=pk) 
        except WatchList.DoesNotExist:
            return Response({'error': 'Not Found'},status=status.HTTP_404_NOT_FOUND)
        watchList = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(watchList)
        return Response(serializer.data)
    
    def put(self, request, pk):
        watchList = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(watchList, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        watchList = WatchList.objects.get(pk=pk)
        watchList.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        