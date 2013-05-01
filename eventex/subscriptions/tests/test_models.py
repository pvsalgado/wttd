# coding: utf-8

from django.test import TestCase
from django.db import IntegrityError
from eventex.subscriptions.models import Subscription
from datetime import datetime

class SubscritionTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name = 'Paulo Vitor Salgado',
            cpf = '1234567890',
            email = 'pv@pv.com',
            phone = '34-99993333'
        )

    def test_create(self):
        'Subscription must have name, cpf, email, phone'
        self.obj.save()
        self.assertEqual(1,self.obj.id)

    def test_has_created_at(self):
        'Subscription must have automatic created_at'
        self.obj.save()
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_unicode(self):
        self.assertEqual(u'Paulo Vitor Salgado', unicode(self.obj))

class SubscriptionUniqueTest(TestCase):
    def setUp(self):
        # Create a first entry to force the colision
        Subscription.objects.create(name='Paulo Vitor Salgado', cpf='1234567891', email='pv@pv.com', phone='34-99993333')

    def test_cpf_unique(self):
        s = Subscription(name='Paulo Vitor Salgado', cpf='1234567891', email='pv@pv.com', phone='34-99993333')
        self.assertRaises(IntegrityError, s.save)

    def test_email_unique(self):
        s = Subscription(name='Paulo Vitor Salgado', cpf='9876543210', email='pv@pv.com', phone='34-99993333')
        self.assertRaises(IntegrityError, s.save)


