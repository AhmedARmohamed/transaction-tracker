from django.test import TestCase
from rest_framework.test import APIClient
from .models import Transaction
from .serializers import TransactionSerializer
from decimal import Decimal
from datetime import date

class TransactionModelTest(TestCase):
    def setUp(self):
        self.transaction = Transaction(
            date=date(2023, 1, 1),
            type="Credit",
            description="Test Transaction",
            debit=Decimal('100.00'),
            credit=Decimal('0.00'),
            balance=Decimal('100.00')
        )
        self.transaction.save()

    def test_transaction_description(self):
        self.assertEqual(str(self.transaction), "Test Transaction")

    def test_transaction_balance(self):
        self.assertEqual(self.transaction.balance, Decimal('100.00'))

class TransactionSerializerTest(TestCase):
    def test_valid_serializer(self):
        data = {
            'date': '01/01/2023',
            'type': 'Credit',
            'description': 'Test Transaction',
            'debit': '100.00',
            'credit': '0.00',
            'balance': '100.00'
        }
        serializer = TransactionSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_serializer_with_invalid_data(self):
        data = {
            'date': '01/01/2023',
            'type': 'Credit',
            'description': 'Test Transaction',
            'debit': 'invalid_debit',  # Invalid data
            'credit': '0.00',
            'balance': '100.00'
        }
        serializer = TransactionSerializer(data=data)
        self.assertFalse(serializer.is_valid())


class TransactionViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.transaction_data = {
            'date': '01/01/2023',
            'type': 'Credit',
            'description': 'Test Transaction',
            'debit': '100.00',
            'credit': '0.00',
            'balance': '100.00'
        }
        self.serializer = TransactionSerializer(data=self.transaction_data)
        if self.serializer.is_valid():
            self.serializer.save()

    def test_get_transaction_list(self):
        response = self.client.get('/transaction/')
        self.assertEqual(response.status_code, 200)

    def test_create_transaction(self):
        response = self.client.post('/transaction/', self.transaction_data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_invalid_transaction_data(self):
        invalid_data = {
            'date': '01/01/2023',
            'type': 'Credit',
            'description': 'Test Transaction',
            'debit': 'invalid_debit',  # Invalid data
            'credit': '0.00',
            'balance': '100.00'
        }
        response = self.client.post('/transaction/', invalid_data, format='json')
        self.assertEqual(response.status_code, 400)
