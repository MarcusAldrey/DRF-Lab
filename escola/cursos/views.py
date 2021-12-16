from rest_framework import request, status
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer


class CursoAPIView(APIView):
  """
  API de Cursos
  """
  
  def get(self, request):
    cursos = Curso.objects.all()
    serializer = CursoSerializer(cursos, many=True)
    return Response(serializer.data)
  
  def post(self, request):
    serializer = CursoSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response({"msg": "Novo curso criado com sucesso"}, status=status.HTTP_201_CREATED)
  
  
class AvaliacaoAPIView(APIView):
  """
  API de Avaliações
  """
  
  def get(self, request):
    avaliacoes = Avaliacao.objects.all()
    serializer = AvaliacaoSerializer(avaliacoes, many=True)
    return Response(serializer.data)
  
  def post(self, request):
    serializer = AvaliacaoSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  