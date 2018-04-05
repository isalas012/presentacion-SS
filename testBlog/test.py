from django.test import TestCase
from .models import article

class articleTest(TestCase):
    def setUp(self):
        print('\n--------------------------test1--------------------------\n')
        #article.objects.create(pk=11, title="Articulo de prueba", content="Este es el contenido de prueba del articulo de prueba", author="Difroggy")
        article.objects.create(pk=11, title="Articulo de prueba", content="Este es el contenido de prueba del articulo de prueba", author="Difroggy")
    def test_article_author(self):
        test_art = article.objects.get(pk=11)
        self.assertEqual(test_art.theAuthor(), "El autor es Difroggy");
        article.objects.create(pk=13, title="Articulo de prueba", content="Este es el contenido de prueba del articulo de prueba", author="Difroggy")
        article.objects.create(pk=13, title="Articulo de prueba", content="Este es el contenido de prueba del articulo de prueba", author="Difroggy")
    def test_stringPK(self):
        article.objects.create(pk="jhon")
