from math import sqrt

'''
Author: Carlos W. Gama
'''
class Recomendacao:

    def __init__(self, base):
        self.baseUsuario = base
        if (type(self.baseUsuario) == list or type(self.baseUsuario) == tuple): self.baseUsuario = self.__converteArrayToDictionary(self.baseUsuario)
        
        self.baseProduto = {}
        self.__geraBaseProduto()

    def comparaExistentes(self, usuario1, usuario2, baseUsuario = True):
        ''' Compara 2 valores existentes da base '''
        base = self.baseUsuario if baseUsuario else self.baseProduto
        return self.__euclidiana(base[usuario1], base[usuario2]) 

    def compararSimNovo(self, existente, novo, baseUsuario = True):
        ''' Compara similaridade de um valor novo a um da base '''
        base = self.baseUsuario if baseUsuario else self.baseProduto
        return self.__euclidiana(base[existente], novo)


    def compararSimNovoTodos(self, novo, baseUsuario = True):
        ''' Compara similaridade de um valor novo a todos da base '''
        todos = []
        novaBase = self.baseUsuario.copy() if baseUsuario else self.baseProduto.copy()
        fitnessNome = 'similaridade' if baseUsuario else 'nota'
        conteudoNome = 'usuario' if baseUsuario else 'produto'
        for existente in novaBase:
            todos.append({conteudoNome: existente, fitnessNome: self.compararSimNovo(existente, novo, baseUsuario), 'dados': novaBase[existente]})
      
        todos.sort(key=lambda v: v[fitnessNome], reverse=True)
        return todos

    def compararExistenteTodos(self, existente, baseUsuario = True):
        ''' Compara similaridade de um valor novo a todos da base '''
        todos = []
        novaBase = self.baseUsuario.copy() if baseUsuario else self.baseProduto.copy()
        conteudoNome = 'usuario' if baseUsuario else 'produto'

        for existenteBase in novaBase:
            if (existenteBase != existente):
                todos.append({conteudoNome: existenteBase, 'similaridade': self.compararSimNovo(existenteBase, novaBase[existente], baseUsuario), 'dados': novaBase[existenteBase]})
      
        todos.sort(key=lambda v: v['similaridade'], reverse=True)
        return todos

    def recomendaBaseadoProduto(self, produto, exibeConteudo = False):
        ''' Retorna lista de produtos baseado em um Produto existente '''
        retorno = self.compararExistenteTodos(produto, False)
        if (not exibeConteudo):
            for i in range(len(retorno)):
                del retorno[i]['dados']
        return retorno

    def recomendaBaseadoEmNota(self, novo):
        ''' Descobre a nota de itens não avaliados '''
        similaridades = self.compararSimNovoTodos(novo)

        novosConteudos = {}
        for usuario in similaridades: #Busca todos da base já com similaridade
            if (usuario['similaridade'] > 0): #Ignora usuários que não possuem similaridades    
                for conteudo in usuario['dados']: #busca os conteúdos do usuário da base
                    if (conteudo not in novo):  #Verifica se é um conteudo não descoberto pelo novo usuário
                        #Caso seja um conteudo ainda não registrado, registra
                        if (conteudo not in novosConteudos):
                            novosConteudos[conteudo] = {'notasTotal': 0, 'similaridadesTotal': 0}
                        
                        novosConteudos[conteudo]['similaridadesTotal'] += usuario['similaridade']
                        novosConteudos[conteudo]['notasTotal'] += usuario['similaridade'] * usuario['dados'][conteudo]

        #print(novosConteudos) #Exibe a lista com notas e similaridades totais de cada conteúdo não visto
        retorno = []
        for c, v in novosConteudos.items():
            retorno.append({'conteudo': c, 'nota': v['notasTotal'] / v['similaridadesTotal']})

        retorno.sort(key=lambda c: c['nota'], reverse=True)
        return retorno

    def __converteArrayToDictionary(self, base):
        ''' Caso os dados tenham sido passados como array, converte para dicionário '''
        return { i : base[i] for i in range(len(base)) }

    def __euclidiana(self, usuario1, usuario2):
        ''' Calcula a distância entre dois valores '''
        #Verifica se há itens em comuns
        diferencaNotas = []
        for item in usuario1:
            if item in usuario2:
                #Adiciona a diferença de notas dos filmes em comuns (Eleva ao quadrado para ficar positivo)
                diferencaNotas.append(pow(usuario1[item] - usuario2[item], 2))

        #Senão encontrou retorna zero de igualdade
        if len(diferencaNotas) == 0: return 0 

        #Retorna a função eu euclidiana dos itens em comuns raiz de (xi²-yi²-zi²)
        distanciaEuclidiana = sqrt(sum(diferencaNotas))
        return 1/(1 + distanciaEuclidiana) #Retorna em porcentagem entre 0 e 1 o nive de igualdade

    def __geraBaseProduto(self):
        baseProduto = {}
        for usuario, produtos in self.baseUsuario.items():
            for produto, nota in produtos.items():
                if (produto not in baseProduto): baseProduto[produto] = {}
                baseProduto[produto][usuario] = nota
        
        self.baseProduto = baseProduto