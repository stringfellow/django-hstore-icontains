from django.test import TestCase
from .models import SomeModel
# Create your tests here.


class IContainsTestCase(TestCase):

    def test_icontains(self):
        SomeModel.objects.create(data={'foo': 'BaR'})

        SomeModel.objects.get(
            data__icontains={'foo': 'bar'}
        )


