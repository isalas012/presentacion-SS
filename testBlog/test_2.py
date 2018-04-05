from django.test import TestCase
from .models import article, comment

class articleCommentTest(TestCase):
    def setUp(self):
        print('\n--------------------------test2--------------------------\n')
        article.objects.create(pk = 14, title="Articulo de prueba2", content="Este es el contenido de prueba del articulo de prueba", author="Difroggy")
        obj = article.objects.create(pk=11, title="Articulo de prueba", content="Este es el contenido de prueba del articulo de prueba", author="Difroggy")
        com = comment.objects.create(pk=11, article = obj, content="Esto es un comentario")
    def test(self):
        com = comment.objects.get(pk=11)
        print(com.cualArticulo())
        self.assertEqual(com.addArticleById(14), True);
        print(com.cualArticulo())
