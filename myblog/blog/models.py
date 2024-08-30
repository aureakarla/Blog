from django.db import models

class Sobre(models.Model):
    biografia = models.TextField(verbose_name="Biografia")
    foto_perfil = models.ImageField(upload_to='imagens/sobre_mim/', null=True, blank=True, verbose_name="Foto de Perfil")

    def __str__(self):
        return "Sobre Mim"

    class Meta:
        verbose_name = "Sobre"
        verbose_name_plural = "Sobre Mim"

class Curso(models.Model):
    nome = models.CharField(max_length=200, verbose_name="Nome do Curso")
    data_conclusao = models.DateField(verbose_name="Data de Conclusão")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

class Interesse(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título do Interesse")

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Interesse"
        verbose_name_plural = "Interesses"
