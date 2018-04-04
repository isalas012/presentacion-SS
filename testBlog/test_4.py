from django.test import TestCase
from .models import article
from django.core.exceptions import ValidationError

class articleTest(TestCase):
    def setUp(self):
        print('--------------------------test4--------------------------')
        file = open("/home/nacho/Documents/SS/presentacion/testBlog/test.txt", 'r')
        for line in file:
            line = line.split('-')
            obj = article(title=line[0], content=line[1], author = line[2])
            try:
                obj.full_clean()
                obj.save()
            except ValidationError as e:
                print(e)

    def test_algo(self):
        todo = article.objects.all()
        for i in todo:
            try:
                self.assertEqual(i.theAuthor(),"El autor es " + i.author)
                print(i.author)
            except Exception as e:
                print(e)
