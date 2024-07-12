from django.db import models

class Marca(models.Model):
    nome = models.CharField(max_length=50)
    nacionalidade = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        if self.nacionalidade:
            return f"{self.nome.upper()} ({self.id}) ({self.nacionalidade})" 
        else:
            return f"{self.nome.upper()} ({self.id})"
    class Meta:
        """Meta options for the model."""

        verbose_name_plural = "Marcas"