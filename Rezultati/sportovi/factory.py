import factory
from factory.django import DjangoModelFactory
from .models import Sport, Natjecanje, Tim, RezultatUtakmice
import random

class SportFactory(DjangoModelFactory):
    class Meta:
        model = Sport
    
    naziv = factory.Sequence(lambda n: f"Sport {n}")


class TimFactory(DjangoModelFactory):
    class Meta:
        model = Tim
    
    naziv = factory.Sequence(lambda n: f"Tim {n}")
    sport = factory.Iterator(Sport.objects.all())


class NatjecanjeFactory(DjangoModelFactory):
    class Meta:
        model = Natjecanje
    
    naziv = factory.Sequence(lambda n: f"Natjecanje {n}")
    sport = factory.Iterator(Sport.objects.all())


class RezultatUtakmiceFactory(DjangoModelFactory):
    class Meta:
        model = RezultatUtakmice

    natjecanje = factory.Iterator(Natjecanje.objects.all())
    domacin = factory.Iterator(Tim.objects.all())
    gost = factory.Iterator(Tim.objects.all())
    rezultat_domacin = factory.Faker('random_int', min=0, max=10)
    rezultat_gost = factory.Faker('random_int', min=0, max=10)


