from django.core.management.base import BaseCommand
from sportovi.models import Sport, Natjecanje, Tim, RezultatUtakmice
from sportovi.factory import SportFactory, NatjecanjeFactory, TimFactory, RezultatUtakmiceFactory
import random

NUM_SPORTS = 5
NUM_NATJECANJA_PER_SPORT = 3
NUM_TIMOVI_PER_SPORT = 10
MIN_TIMOVI_PER_NATJECANJE = 2
MAX_TIMOVI_PER_NATJECANJE = 4

class Command(BaseCommand):
    help = "Generates test data for sports app"

    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        Sport.objects.all().delete()
        Natjecanje.objects.all().delete()
        Tim.objects.all().delete()
        RezultatUtakmice.objects.all().delete()

        self.stdout.write("Creating new data...")

        for i in range(NUM_SPORTS):
            sport = SportFactory()
            print(f"Created Sport: {sport.naziv}")

            natjecanja = [NatjecanjeFactory(sport=sport) for _ in range(NUM_NATJECANJA_PER_SPORT)]
            timovi = [TimFactory(sport=sport) for _ in range(NUM_TIMOVI_PER_SPORT)]

            for natjecanje in natjecanja:
                print(f" Natjecanje: {natjecanje.naziv}, Sport: {natjecanje.sport.naziv}")

                odabrani_timovi = random.sample(timovi, random.randint(MIN_TIMOVI_PER_NATJECANJE, min(MAX_TIMOVI_PER_NATJECANJE, len(timovi))))
                natjecanje.tim.set(odabrani_timovi)
                print(f"  Timovi dodijeljeni natjecanju '{natjecanje.naziv}': {[tim.naziv for tim in odabrani_timovi]}")

                for domacin in odabrani_timovi:
                    for gost in [t for t in odabrani_timovi if t != domacin]:
                        rezultat_utakmice = RezultatUtakmiceFactory(natjecanje=natjecanje, domacin=domacin, gost=gost)
                        print(f"   Rezultat Utakmice: {rezultat_utakmice.domacin.naziv} vs {rezultat_utakmice.gost.naziv} - {rezultat_utakmice.rezultat_domacin}:{rezultat_utakmice.rezultat_gost}")

        self.stdout.write(self.style.SUCCESS("Test data successfully created."))