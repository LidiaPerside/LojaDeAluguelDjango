# Loja de Aluguel utilizando Django
## Há uma utilização do SQLite

### O código funciona da seguinte maneira:
Os usuários cadastrados podem adicionar itens para alugar, fazer alterações e deletar. 
Cada usuário tem acesso apenas aos seus itens.

#### Até o momento, a aplicação funciona da forma abaixo:
Existe uma espécie de agenda de locação e só será exibido as reservas cadastradas no horário de agora em diante. 
Os que foram cadastrados abaixo da data do momento, não serão exibidos - com excessão de reservas passadas com até 1 hr, que serão exibidos com a cor vermelha.

