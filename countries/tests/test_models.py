# -*- coding: utf-8 -*-
from django.test import TestCase
from django.utils.six import text_type
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

    def test_text_type(self):
        name = u'日本'
        country = CountryFactory.build(name=name)
        self.assertEqual(text_type(country), name)
