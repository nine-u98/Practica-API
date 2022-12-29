from django.shortcuts import render
from .models import Services
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import ServiceSerializer
from rest_framework.response import Response
from .pagination import StandardResultsSetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAdminUser


# Create your views here.
class ServiceViewSet_v1(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class= ServiceSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('name', 'description')
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticated]


class ServiceViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    queryset = Services.objects.all()
    pagination_class= StandardResultsSetPagination

    def get_permissions(self):
        if self.action not in ['destroy','partial_update','update','create']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]


class GetAllServiceView(APIView):
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    def get(self, request):
        services = Services.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)
