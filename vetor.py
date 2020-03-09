from recomendacao import Recomendacao

#0 = Não viu | 1 = Viu | 2 = Comprou
produtosPorUsuarios = [
    {'a':1, 'b': 0, 'c':0, 'd':1, 'e':2, 'f':2},
    {'a':2, 'b': 1, 'c':1, 'd':0, 'e':0, 'f':2},
    {'a':2, 'b': 2, 'c':0, 'd':0, 'e':1, 'f':0},
    {'a':0, 'b': 2, 'c':2, 'd':1, 'e':1, 'f':0},
    {'a':1, 'b': 0, 'c':0, 'd':2, 'e':1, 'f':1},
    {'a':0, 'b': 0, 'c':2, 'd':2, 'e':1, 'f':2},
    {'a':2, 'b': 1, 'c':0, 'd':1, 'e':2, 'f':1},
    {'a':1, 'b': 1, 'c':1, 'd':0, 'e':2, 'f':2},
    {'a':0, 'b': 1, 'c':0, 'd':1, 'e':1, 'f':0},
    {'a':0, 'b': 0, 'c':0, 'd':2, 'e':1, 'f':0},
    {'a':2, 'b': 2, 'c':2, 'd':0, 'e':2, 'f':0},
    {'a':1, 'b': 0, 'c':2, 'd':1, 'e':2, 'f':2},
    {'a':1, 'b': 1, 'c':0, 'd':2, 'e':1, 'f':1},
    {'a':2, 'b': 2, 'c':1, 'd':1, 'e':2, 'f':2},
    {'a':0, 'b': 2, 'c':1, 'd':0, 'e':0, 'f':2},
    {'a':0, 'b': 0, 'c':0, 'd':0, 'e':0, 'f':0},
    {'a':2, 'b': 0, 'c':2, 'd':1, 'e':2, 'f':0},
    {'a':1, 'b': 1, 'c':0, 'd':0, 'e':2, 'f':2},
]

rc = Recomendacao(produtosPorUsuarios)

print('Recomendação por acesso:')
print(rc.recomendaBaseadoEmNota({'a': 0, 'b': 0, 'd': 2, 'e': 2}))

print('Recomendação por produto: ')
print(rc.recomendaBaseadoProduto('a'))

