'''
Creando el CRUD de usuarios
'''
from rest_framework.serializers import ModelSerializer
from users.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model  = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password', 'is_active', 'is_staff']
