print('Conversor de horas ')
"""Vai começar de 13 horas ate 00:00 horas """

lista_1=[13,14,15,16,17,18,19,20,21,22,23]
lista_2=[1,2,3,4,5,6,7,8,9,10,11]

horario=int(input('Selecione a hora '))
minuto=input('Escolha os minutos')

if horario in lista_1 :
    loc = lista_1.index(horario)
    print(f'O horario selecionado pelo usuario é de {horario} horas e {minuto} minutos')
    print(f'O numero com a conversão realizada fica em {lista_2[loc]} PM  e {minuto} minutos ')
else:
    print('Não foi necessario aplicar conversão de AM para PM')
    print(f'O horario informado então é de {horario} horas e {minuto} minutos')





