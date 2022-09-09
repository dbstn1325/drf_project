from wsgiref.validate import validator
from rest_framework import serializers

from watchlist_app.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    active_status = serializers.SerializerMethodField()
    
    class Meta:
        model = Movie
        fields = '__all__'
        # fields = ['id', 'name', 'description', 'active']
        # exclude = ['active']
        
    def get_active_status(self, obj):
        if obj.active == True:
            return "존재하는 팔드"
        else:
            return "존재하지 않는 필드"
        

    # 객체를 가져와서 걸려줄수도도있다!!
    def validate(self, value):
        if value['description'] == value['name']:
            raise serializers.ValidationError("내용과 이름과 같으면 안돼여")
        else:
            return value
    
    # validate_[이름] => 생성할때, 감시자가 들어온 데이터를 여기서도 걸러주는거 가능하다!
    def validate_description(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("내용의 길이가 너무 짧습니다.")
        else:
            return value
        
    
    

# def validate_name(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("이름이 너무 짧아용!!")
#     else:
#         return value

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[validate_name])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
#     # validated_data 는 name, description, active를 의미한다.
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
    
#     # 객체를 가져와서 걸려줄수도도있다!!
#     def validate(self, value):
#         if value['description'] == value['name']:
#             raise serializers.ValidationError("내용과 이름과 같으면 안돼여")
#         else:
#             return value
    
#     # validate_[이름] => 생성할때, 감시자가 들어온 데이터를 여기서도 걸러주는거 가능하다!
#     # def validate_description(self, value):
#     #     if len(value) < 2:
#     #         raise serializers.ValidationError("내용의 길이가 너무 짧습니다.")
#     #     else:
#     #         return value
        
    