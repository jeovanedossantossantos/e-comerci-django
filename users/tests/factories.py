import factory
import factory.fuzzy

from ..models import User

class UserFactory(factory.django.DjangoModelFactory):
    name = factory.fuzzy.FuzzyText()
    email = factory.fuzzy.FuzzyText()
    password = factory.fuzzy.FuzzyText()
    type = factory.fuzzy.FuzzyText()

    class Meta:
        model = User