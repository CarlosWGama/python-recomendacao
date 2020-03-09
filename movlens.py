import pandas as pd
from recomendacao import Recomendacao
filmes = pd.read_csv('./movlens/filmes.csv', sep='|')
notas = pd.read_csv('./movlens/notas.csv', sep='|')
usuarios = notas.values
#Base de notas
base = {}
for i in range(len(usuarios)):
    #[codigo do usuario][codigo do filme] = nota
    if (usuarios[i][1] not in base): base[usuarios[i][1]] = {}
    base[usuarios[i][1]][usuarios[i][0]] = usuarios[i][2]

#Filmes
filmes = filmes.values


#Recomendação Baseada em Notas
print('Recomendação baseado em Nota:')
rc = Recomendacao(base)
fRec = rc.recomendaBaseadoEmNota({242:5, 78:3, 875:3.5})
fRec = fRec[0:5]
for filme in fRec:
    print('Filme: ', filmes[filme['conteudo']-1][1], ' - Nota: ', filme['nota'])

print("------------------------------------")
codFilme = 50
print('Recomendação baseado em Filme:', filmes[codFilme-1][1])
#Recomenda Baseado em Produto
fRec = rc.recomendaBaseadoProduto(codFilme) 
fRec = fRec[0:5]
for filme in fRec:
    print('Filme: ', filmes[filme['produto']-1][1], ' - Nota: ', filme['similaridade'])
    
