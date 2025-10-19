from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer, UserSerializer as BaseUserSerializer


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id','email','password','first_name','last_name','address','phone_number','role']

class SimpleStudentSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['email','first_name','last_name','address','phone_number']
        read_only_fields = ['role']

class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        ref_name ='CustomUser'
        fields = ['id','email','first_name','last_name','address','phone_number','role']
        read_only_fields = ['role']