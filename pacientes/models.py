from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=155)
    data_de_nascimento = models.DateField()
    cpf = models.CharField(max_length=155)

    def __str__(self) -> str:
        return self.nome