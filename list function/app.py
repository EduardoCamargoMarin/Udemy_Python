
numeros =[3,4,6,7,11,5,1,77,55,44,33]
amigos = ['Andreia', 'Julia', 'Caio', 'Julio', 'Rodrigo']

amigos.extend(numeros) #colocar duas listas juntas
amigos.append('João') #adiciona um nome item na lista
amigos.insert(1,'Carlos') #adiciona em um ponto especifico
amigos.remove('Rodrigo') #remove um item da lista
amigos.pop(2) #remove um item pelo index da lista
print(amigos)
print(amigos.index('Caio')) #checa qual index o item se encontra
print(amigos.count('Andreia')) #conta quantos itens tem a mesma sintaxe na lista
print(numeros.sort())



