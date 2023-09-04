from django.test import TestCase
from .models import Coche

class CocheTestCase(TestCase):
    def setUp(self):
        Coche.objects.create(marca="Toyota", modelo="Camry", año=2020, descripcion="Coche deportivo", precio=25000)

    def test_coche_str(self):
        coche = Coche.objects.get(modelo="Camry")
        self.assertEqual(str(coche), "Camry")

