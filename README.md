# Jogo da velha

> criar uma aplicação de terminal que simule um jogo da velha

## Tabuleiro

O tabuleiro deve ser exibido da seguinte forma:
```shell
       |       |       
       |       |       
_______|_______|_______
       |       |       
       |       |       
_______|_______|_______
       |       |       
       |       |       
       |       |       
```

Cada quadrado será composto como 7 espaços de largura por 3 espaços de altura, tendo o underscore(_) e pipe (|) como limitantes:
```shell
       |
       |
_______|
```

As posições ocupadas devem ser marcadas com "X" ou "O" no centro de cada quadrado:
```shell
       |       |       
   X   |   O   |   O   
_______|_______|_______
```

## Criar função que monte o tabuleiro

Pode optar por realizar os prints de forma manual ou tentar fazer uso de estrutura de repetição FOR

```python
def buildBoard():
    print("board")
```

## Registro de jogadas

Através do comando de entrada de dados, salvar as jogadas de forma que seja possível validar se o jogo acabou

```python
def nextMove():
    playerMove = input("Qual o proximo movimento? ")

```
