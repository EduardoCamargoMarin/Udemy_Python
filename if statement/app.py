
acordei_antes_9 = True
fome = True

if acordei_antes_9 and fome: #o and funciona da mesma maneira que o &&, pode adicionar o elif se precisar. se for usar || substitua por or
    print('Hora de fazer o café da manhã')

elif acordei_antes_9 and not(fome): #condição de negação
    print('Hora de fazer uma corrida')


else:
    print('Faça o almoço')

