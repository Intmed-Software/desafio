from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.conf import settings

class ClienteView(APIView):

    def post(self, request):
        nome = request.data['nome']
        email = request.data['email']
        senha = request.data['senha']
        senha_confirma = request.data['senha_confirma']

        print(request.data)

        print("Verificar senha")
        if not senha == senha_confirma:
            return Response({'msg': 'A senha e a confirmação de senha estão diferentes!'}, status=400)

        print("Verificar nome")
        if nome == '' or nome == None:
            return Response({'msg': 'O campo nome está em branco!'}, status=400)

        print("Verificar E-mail")
        if email == '' or email == None:
            return Response({'msg': 'O campo email está em branco!'}, status=400)

        nome = nome.split(' ')

        user = User()
        user.username = email
        user.email = email
        user.first_name = nome[0]
        user.last_name = nome[len(nome)-1] if len(nome) > 1 else ""
        user.password = make_password(senha)
        user.superuser = False
        user.is_staff = False
        user.is_active = True

        print("Salvar Usuário")
        user.save()

        return Response({
            'id': user.id,
            'nome': user.first_name + " " + user.last_name,
            'email': user.email,
        }, status=201)


class MyAcountView(APIView):
    permission_classes = (IsAuthenticated,)
    def get (self, request):
        user = request.user
        return Response({ 
            'id': request.user.id,
            'email': request.user.email,
            'usuario': request.user.username,
            'nome': request.user.first_name + " " + request.user.last_name
        })
