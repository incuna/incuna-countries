import factory

from ..models import Country


class CountryFactory(factory.DjangoModelFactory):
    name = factory.Sequence('Country {}'.format)
    code = factory.Sequence('{}'.format)

    class Meta:
        model = Country
