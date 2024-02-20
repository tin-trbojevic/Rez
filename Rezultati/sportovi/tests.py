from django.test import TestCase, SimpleTestCase
from sportovi.models import *
from sportovi.forms import *
from django.urls import reverse, resolve
from sportovi.factory import *
from sportovi.views import *

class SportModelTest(TestCase):
    def setUp(self):
        Sport.objects.create(naziv='Nogomet')

    def test_sport_creation(self):
        sport = Sport.objects.get(naziv='Nogomet')
        self.assertTrue(isinstance(sport, Sport))
        self.assertEqual(sport.__str__(), sport.naziv)


class SportFormTest(TestCase):
    def test_sport_form_valid(self):
        form_data = {'naziv': 'Nogomet'}
        form = SportForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_sport_form_invalid(self):
        form_data = {'naziv': ''}
        form = SportForm(data=form_data)
        self.assertFalse(form.is_valid())


class SportoviListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_sports = 5
        for sport_num in range(number_of_sports):
            Sport.objects.create(naziv=f'Sport {sport_num}')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/sportovi/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('sportovi:sportovi_list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('sportovi:sportovi_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'glavni/sportovi_list.html')

    def test_pagination_is_five(self):
        response = self.client.get(reverse('sportovi:sportovi_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('sportovi' in response.context)
        self.assertTrue(len(response.context['sportovi']) == 5)


class FactoryTest(TestCase):
    def setUp(self):
        self.sport = SportFactory()
        self.tim = TimFactory(sport=self.sport)
        self.natjecanje = NatjecanjeFactory(sport=self.sport)

    def test_sport_factory(self):
        sport = SportFactory()
        self.assertTrue(isinstance(sport, Sport))
        self.assertTrue(sport.naziv.startswith('Sport '))

    def test_tim_factory(self):
        tim = TimFactory(sport=self.sport)
        self.assertTrue(isinstance(tim, Tim))
        self.assertTrue(tim.naziv.startswith('Tim '))
        self.assertEqual(tim.sport, self.sport)

    def test_natjecanje_factory(self):
        natjecanje = NatjecanjeFactory(sport=self.sport)
        self.assertTrue(isinstance(natjecanje, Natjecanje))
        self.assertTrue(natjecanje.naziv.startswith('Natjecanje '))
        self.assertEqual(natjecanje.sport, self.sport)

    def test_rezultat_utakmice_factory(self):
        rezultat_utakmice = RezultatUtakmiceFactory(natjecanje=self.natjecanje, domacin=self.tim, gost=TimFactory(sport=self.sport))
        self.assertTrue(isinstance(rezultat_utakmice, RezultatUtakmice))
        self.assertEqual(rezultat_utakmice.natjecanje, self.natjecanje)
        self.assertEqual(rezultat_utakmice.domacin, self.tim)


class TestUrls(SimpleTestCase):
    def test_homepage_url(self):
        url = reverse('sportovi:homepage')
        self.assertEqual(resolve(url).func, homepage)

    def test_sportovi_list_url(self):
        url = reverse('sportovi:sportovi_list')
        self.assertEqual(resolve(url).func.view_class, SportoviListView)

    def test_create_sport_url(self):
        url = reverse('sportovi:create_sport')
        self.assertEqual(resolve(url).func.view_class, CreateSport)