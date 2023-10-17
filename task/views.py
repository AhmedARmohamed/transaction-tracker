from rest_framework import generics
from .models import Transaction
from .serializers import TransactionSerializer
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination

class TransactionView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['date', 'description']
    ordering_fields = ['date', 'description']
    ordering = ['date']


    def create(self, request, *args, **kwargs):
        payload = request.data
        serializer = TransactionSerializer(data=payload, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('ok')
