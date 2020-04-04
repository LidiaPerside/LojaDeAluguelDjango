from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#Tabela de Itens

class Itens (models.Model):
    item = models.CharField(max_length=100)
    tipo_item = models.TextField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    nome_cliente = models.TextField(max_length=100, blank= True, null=True)
    data_aluguel = models.DateTimeField(verbose_name="Data do Aluguel")
    data_criacao = models.DateTimeField(auto_now = True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    #python manage.py makemigrations core
    #python manage.py sqlmigrate core 0002
    #python manage.py migrate core 0002

    class Meta:
        db_table = 'item'

    def _str_(self):
        return self.item

    def get_data_aluguel(self):
        return self.data_aluguel.strftime('%d/%m/%Y %H:%M hrs')


    #reservaitem
    #cancelarreserva
    #alugaritem
    #devolução de item

    #opcional:
    #itens a serem devolvidos na semana, junto com os valores semanais
    #itens alugados no periodo semanal, junto com os valores