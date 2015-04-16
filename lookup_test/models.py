from django.db import models

from django_hstore import hstore


class SomeModel(models.Model):
    data = hstore.DictionaryField(blank=True)
    objects = hstore.HStoreManager()
