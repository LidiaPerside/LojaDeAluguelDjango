from django.contrib import admin
from core.models import Itens
# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    list_display = ('item', 'data_aluguel', 'data_criacao')
    list_filter = ('item','data_aluguel',)

admin.site.register(Itens, ItemAdmin)