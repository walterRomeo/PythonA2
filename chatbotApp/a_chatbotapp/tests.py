from django.test import TestCase

# Create your tests here.
from django.test import Client
from django.urls import reverse

def test_add():
    client = Client()
    response  = client.post(reverse(viewname='add'),
                            {'num01':'2', 'num02':2},
                            HTTP_AUTHORIZATION='JIRNO9328YR79IHFIJUOISDHFIW97FT89WOFYHIUSWGF')
    assert response.status_code ==200 and float(response.content) == 0

