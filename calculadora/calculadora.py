import os
import time

def slowprint(texto, atraso=0.2):
  for c in texto:
    print(c,end='',flush=True)
    time.sleep(atraso)

time.sleep(1.2)
nome = input('Qual o seu nome?\n')
os.system('cls')

print ('Olá, ', nome)
time.sleep(1.2)

os.system('cls')
slowprint('ISTO É UMA SIMULAÇÃO DE CALCULADORA?\n')

num_1 = float(input('Digite seu primeiro número:\n'))
num_2 = float(input('Digite seu segundo número:\n'))
os.system('cls')

operador = float (input ('Qual operação deseja fazer: \n1-Adição\n2-Subtração\n3-Multiplicação\n4-Divisão\n'))

if operador == 1:
    print('Seu resultado é: ', num_1 + num_2)
elif  operador == 2 :
    print('Seu resultado é: ', num_1 - num_2)
elif operador == 3:
    print('Seu resultado é: ', num_1 * num_2) 
else: slowprint('Seu resultado é: ', num_1 / num_2)