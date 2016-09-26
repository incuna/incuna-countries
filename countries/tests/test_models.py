# -*- coding: utf-8 -*-
from django.test import TestCase
from incuna_test_utils.utils import field_names

from .factories import CountryFactory
from ..models import Country


class TestCountry(TestCase):
    def test_fields(self):
        fields = field_names(Country)
        expected = {
            'code',
            'id',
            'name',
        }

        self.assertEqual(fields, expected)

    def test_str(self):
        name = 'Japan'
        country = CountryFactory.build(name=name)
        self.assertEqual(str(country), name)

    def test_unicode(self):
        name = u'日本'
        country = CountryFactory.build(name=name)
        self.assertEqual(unicode(country), name)
