from django.contrib.auth.models import User
from rest_framework import serializers

class RegistraionSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
    def save(self):
        
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        
        # 비밀번호 불일치 처리
        if password != password2:
            raise serializers.ValidationError({'error': '비밀번호가 서로 일치하지 않습니다.'})
    
        # 이메일 중복 처리 (User => admin 페이지의 Users에 등록된 이메일과 확인한다.)
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error': '이미 존재하는 이메일 입니다.'})
        
        account = User(email=self.validated_data['email'], username=self.validated_data['username'])
        account.set_password(password)
        account.save()
        
        return account