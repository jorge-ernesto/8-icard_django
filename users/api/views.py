'''
Creando el CRUD de usuarios
'''
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from users.models import User
from users.api.serializers import UserSerializer

class UserApiViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]  # crud de usuarios - solo los administradores (superusuario, staff) pueden acceder a estas vistas.
    serializer_class   = UserSerializer
    queryset           = User.objects.all()

    '''
    Override de la creación de usuario
    '''
    def create(self, request, *args, **kwargs):
        # esta línea actualiza la contraseña del usuario en los datos de solicitud con un hash seguro generado por la función make_password.
        request.data['password'] = make_password(request.data['password'])

        # esta línea llama a la función create del padre (ModelViewSet) para crear el objeto de usuario utilizando los datos de solicitud actualizados.
        return super().create(request, *args, **kwargs)

    '''
    Override de la actualización del usuario
    '''
    def partial_update(self, request, *args, **kwargs):
        # extrae el valor del campo "password" de los datos de la solicitud (request)
        password = request.data['password']
        
        # Verificar data
        print('request user', request.user)
        print('request user password', request.user.password)
        print('request data', request.data)
        print('make_password', make_password(password))

        # verifica si el valor de "password" esta definido y no es nulo o vacío
        if password:
            # print('Cambio de contraseña')
            request.data['password'] = make_password(password)
        else:
            # print('Mantiene la contraseña')
            request.data['password'] = request.user.password

        # reescribe la funcion partial_update
        return super().partial_update(request, *args, **kwargs)

'''
Creando endpoint para obtener los datos personales
'''
class UserView(APIView):
    permission_classes = [IsAuthenticated]  # datos personales - solo los usuarios autenticados pueden acceder a esta vista.

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
