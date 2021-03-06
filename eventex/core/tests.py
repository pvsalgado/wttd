# coding: utf-8
from django.test import TestCase


class HomepageTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')

    def test_get(self):
        'GET / must retrun status 200.'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'homepage muste usu template index.html'
        self.assertTemplateUsed(self.resp, 'index.html')
