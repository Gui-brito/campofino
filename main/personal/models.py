from django.db import models
from django.urls import reverse
from django.http import HttpResponse

def local_upload(request, filename):
	file_path = 'profile/{filename}'.format(filename=filename)
	return file_path

class Produtos(models.Model):
    produto_name              = models.CharField(max_length=32, verbose_name="Nome do Produto")
    descricao                 = models.TextField(max_length=300, verbose_name="Descrição do Produto")
    status                    = models.BooleanField(default=True, verbose_name="Status do Produto")
    data_insercao             = models.DateTimeField(verbose_name="Data de Inserção", auto_now_add=True)
    imagem                    = models.ImageField(upload_to=local_upload, verbose_name="Imagem do Produto")

    def __str__(self):
        return self.produto_name
    
    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "(01) - Produtos"

class Carrosel(models.Model):
    imagem_name               = models.CharField(max_length=32, verbose_name="Nome da Imagem")
    imagem                    = models.ImageField(upload_to=local_upload, verbose_name="Imagem do Produto")

    def __str__(self):
        return self.imagem_name
    
    class Meta:
        verbose_name = "Imagem"
        verbose_name_plural = "(02) - Imagens"


