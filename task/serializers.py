from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    date = serializers.DateField(input_formats=['%d/%m/%Y'])
    class Meta:
        model = Transaction
        fields = "__all__"
