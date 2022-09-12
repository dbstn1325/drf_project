from watchlist_app.api.serializers import StreamPlatformSerializer, WatchListSerializer
from watchlist_app.models import WatchList, StreamPlatform
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

class StreamPlatformAV(APIView):
    
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

    
    

class WatchListAV(APIView):
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
        
        

# @api_view(['GET', 'POST'])
# def WatchList_list(request):
#     try:
#         WatchList = WatchList.objects.get(pk=pk) 
#     except WatchList.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         WatchLists = WatchList.objects.all()
#         serializer = WatchListSerializer(WatchLists, many=True)
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer = WatchListSerializer(data=request.data)
#         # validated_data에 딱맞게 들어왔다면,
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=400)

# @api_view(['GET', 'PUT', 'DELETE'])
# def WatchList_detail(request,pk):
#     try:
#         WatchList = WatchList.objects.get(pk=pk)
#     except WatchList.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         WatchList = WatchList.objects.get(pk=pk)
#         serializer = WatchListSerializer(WatchList)
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         WatchList = WatchList.objects.get(pk=pk)
#         serializer = WatchListSerializer(WatchList, request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
        
#         else:
#             return Response(serializer.errors, status=400)
    
#     if request.method == 'DELETE':
#         WatchList = WatchList.objects.get(pk=pk)
#         WatchList.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)