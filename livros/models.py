from django.db import models

class Livros(models.Model):
    #id_books = models.UUIDField(primary_key=True,default=uuid)
    titulo= models.CharField("titulo", max_length = 80)
    autor= models.CharField("autor", max_length=80)
    ano_lancamento=models.IntegerField()
    status = models.CharField("status", max_length=80)
    paginas= models.IntegerField()
    companhia= models.CharField("companhia", max_length=80)
    #data_criacao= models.DataTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    class Meta:
        db_table = 'Livros'
        managed = True
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
# Create your models here.
