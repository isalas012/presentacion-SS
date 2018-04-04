from django.db import models

# Create your models here.

class article(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    author = models.CharField(max_length=50, default="anónimo")
    def theAuthor(self):
        return ("El autor es " + self.author)
    def editar(self, title=None, content=None, author=None):
        if title !=None:
            self.title = title
        if content !=None:
            self.content = content
        if author != None:
            self.author = author
        return True



class comment(models.Model):
    article = models.ForeignKey(article, on_delete=models.CASCADE,)
    content = models.CharField(max_length=200)
    author = models.CharField(max_length=50, default="anónimo")
    def addArticleById(self, id):
        self.article = article.objects.get(pk = id)
        return True
    def cualArticulo(self):
        return "Este comentario pertenece al articulo " + self.article.title
