from django.test import TestCase
from .models import article

class articleTest(TestCase):
    def setUp(self):
        print('--------------------------test3--------------------------')
        article.objects.create(pk=11, title="Articulo de prueba", content="Este es el contenido de prueba del articulo de prueba", author="Difroggy")
    def test_article_author(self):
        test_art = article.objects.get(pk=11)
        self.assertEqual(test_art.editar(title="Este es un nuevo titulo"), True);
