from user_app.api.serializers import RegistraionSerializer
from user_app import models

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status

@api_view(['POST',])
def logout_view(request):
    
    if request.method == 'POST':
        # 현재 로그인한 유저(request.user)
        request.user.auth_token.delete()
        return Response(status= status.HTTP_200_OK)

@api_view(['POST',])
def registration_view(request):
    
    if request.method == 'POST':
        serializer = RegistraionSerializer(data=request.data)
        
        data = {}
        
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "유저 등록 성공!!"
            data['username'] = account.username
            data['email'] = account.email
            # serializer의 save()메서드로 착착 저장된 애들(account)을 다시가져와서 조회한다.
            token = Token.objects.get(user=account).key
            data['token'] = token        
        else:
            data = serializer.errors
        
        return Response(data)