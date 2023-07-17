print('~=' * 20)
print('Ex: 01')
print('~=' * 20)

t = int(input('Qual a temperatura da carne? '))

if t <= 47:
    print('A carne precisa de mais algum tempo no fogo')

elif t in range(48, 54):
    print('A carne está mal passada')

elif t in range(54, 60):
    print('A carne está no ponto para mal passada')

elif t in range(60, 65):
    print('A carne está ao ponto')

elif t in range(65, 71):
    print('A carne está no ponto para bem')

elif t in range(71, 76):
    print('A carne está bem passada')

elif t > 76: 
    print('A carne ficou bastante tempo no fogo, talvez tenha dificuldade de comer')
    


print('~=' * 20)
print('Ex: 02')
print('~=' * 20)

r = int(input('Qual é o rendimento da lata? '))
a = int(input('Qual é a altura da parede? '))
l = int(input('Qual é a largura da parede? '))

def calculo_Tinta():
    area = (a * l) / r 
    print(f'Você precisa de {a} latas de tinta.')

calculo_Tinta()



print('~=' * 20)
print('Ex: 03')
print('~=' * 20)

funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa']
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turno_noite = ['Pedro', 'Sophia', 'Bruno']
tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']

lista1 = set(tem_carro).intersection(turno_noite)
print(lista1)

lista2 = set(tem_carro).intersection(turno_dia)
print(lista2)

lista3 = set(funcionarios).difference(tem_carro)
print(lista3)



print('~=' * 20)
print('Ex: 04')
print('~=' * 20)

a = float(input('Qual a sua altura em cm? '))
p = float(input('Qual é o seu peso em kg? '))

imc = p / (a/100)**2
print(f'Seu IMC é {round(imc, 2)}.')

if imc < 18.59:
    print('Magreza')

elif imc >=18.59 and imc < 24.99:
    print('Seu peso está normal')

elif imc >= 25.00 and imc < 29.99:
    print('Está com sobrepeso')

elif imc >= 30.00 and imc < 39.99:
    print('Está com obesidade')

else:
    print('Está com obesidade grave')



print('~=' * 20)
print('Ex: 05')
print('~=' * 20)

frutas = ['Maçã', 'Banana', 'Manga', 'Uva']
frutas.append('Abacaxi')
frutas.extend(['Abacate', 'Morango', 'Melancia'])
frutas.remove('Manga')
frutas.pop()
print(frutas[0], 'e', frutas[2])
print(frutas)

for fruta in frutas:
    print(f'Eu gosto de {fruta}.')

'''

'''
print('~=' * 20)
print('Ex: 06')
print('~=' * 20)

for x in range(1, 11):
    print(x, end=' ')

print(' ')

for x in range(1, 20, 4):
    print(x, end=' ')




print('~=' * 20)
print('Ex: 07')
print('~=' * 20)

frutas = ['Maçã', 'Banana', 'Manga']
verduras = ['Repolho', 'Alface', 'Brócolis']

for fruta in frutas:
    for verdura in verduras:
        print(fruta, verdura)



print('~=' * 20)
print('Ex: 08')
print('~=' * 20)

x = 1
while x <= 10:
    print(x)
    x += 1

  

print('~=' * 20)
print('Ex: 09')
print('~=' * 20)

print('Loop com break: ')
for num in range(1, 11):
    if num > 5:
        break
    print(num)

print('\nLoop com continue: ')
for num in range (1, 11):
    if num  == 5:
        continue
    print(num)

 

print('~=' * 20)
print('Ex: 10')
print('~=' * 20)

frutas = ['Maçã', 'Maçã', 'Maçã', 'Laranja', 'Morango', 'Pera', 'Uva', 'Melancia']

contador = 0
for fruta in frutas: 
    if fruta == 'Maçã':
        contador += 1 

print('Número de maçãs na lista é: ', contador) 



print('~=' * 20)
print('Ex: 11')
print('~=' * 20)

n = int(input('Digite qualquer número inteiro: '))

if n > 10:
    print (f'O número {n} é maior do que 10.')

elif n == 10:
    print (f'O número {n} é igual a 10.')

else: 
    print(f'O número {n} é menor do que 10.')
 


print('~=' * 20)
print('Ex: 12')
print('~=' * 20)

idade = int(input('Digite a sua idade: '))

if idade < 13:
    print (f'Você ainda tem {idade} anos, e não pode acessar!')

elif 13 <= idade <= 19:
    print(f'Você tem {idade} anos, e ainda é um adolescente, falta pouco para conseguir acessar.')
else: 
    print(f'Você tem {idade} anos, e portanto, já pode acessar!') 



print('~=' * 20)
print('Ex: 13')
print('~=' * 20)

loja = ['BMW X6', 'BMW i5', 'BMW i8']

carro = input('Qual carro deseja comprar? ')
if carro in loja:
    print(f'Temos o carro {carro} em estoque.')
else:
    print(f'Não temos o {carro} em estoque. O prazo para entrega é de 20 dias')




print('~=' * 20)
print('Ex: 14')
print('~=' * 20)

while True: 
    n = input('Adivinha qual fruta estou pensando: ').lower().strip()
    if n == 'abacate':
        print('Acertou!!! Parabéns!')
        break

    
       
print('~=' * 20)
print('Ex: 15')
print('~=' * 20)

#n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = list(rang(1,11))
for x in n:
    if x % 2 == 0:
        print(f'O número {x} é par.')
    else: 
        print(f'O número {x} é impar.')



print('~=' * 20)
print('Ex: 16')
print('~=' * 20)

n = int(input('Escolha um número para saber se é par ou ímpar: '))

if n % 2 == 0:
    print(f'O número {n} é par.')
else: 
    print(f'O número {n} é ímpar.')


    
print('~='*20)
print('Ex: 17')
print('~='*20)

cidades = ('são paulo', 'rio de janeiro', 'salvador')
n = input('Digite uma cidade do Brasil: ').lower().strip()

if n in cidades:
  print(f'A cidade {n} está na lista.')
else:
  print(f'A cidade {n} não está na lista.')



print('~='*20)
print('Ex: 18')
print('~='*20)

capitais = {
  'Brasil': 'Brasília',
  'Portugal' : 'Lisboa',
  'Estados Unidos' : 'Washington',
  'Chile' : 'Santiago',
  'Canada' : 'Ottawa' }

p = input('Digite um país: ')

if p in capitais:
  print(f'O país digitado foi {p}, e sua capital é {capitais[p]}.')

else:
  print('O país não está na lista.')



print('~='*20)
print('Ex: 19')
print('~='*20)

amigos1 = {'Roberta', 'Luiz', 'Leticia', 'Rone', 'Renata'}
amigos2 = {'Jose', 'Roberta', 'Luiz', 'Carol', 'Paulo'}

x = amigos1.intersection(amigos2)
y = amigos1.union(amigos2)
z = amigos1.difference(amigos2)
print(x)
print(y)
print(z)



print('~='*20)
print('Ex: 20')
print('~='*20)


x = int(input('Digite um número inteiro qualquer: '))
#pode ser feito assim
y = x**2
print(f'O quadrado do número {x} é {y}.')
#pode ser feito assim
print(f'O quadrado do número {x} é {x**2}')

#pode ser feito assim
def quadrado (n):
  return n**2
numero = int(input('Digite um número inteiro qualquer: '))
print(f'O quadrado do número {numero} é {quadrado(numero)}')

 

print('~='*20)
print('Ex: 21')
print('~='*20)

def soma (n1, n2):
  return n1 + n2  
usuario_n1 = int(input('Digite um número: '))
usuario_n2 = int(input('Digite outro número: '))
print(f'A soma do número {usuario_n1} e do número {usuario_n2} é {soma(usuario_n1, usuario_n2)}')



print('~='*20)
print('Ex: 22')
print('~='*20)

def potencia(base, expoente):
  return base ** expoente

num_base = int(input('Digite o número da base: '))
num_expoente = int(input('Digite o expoente desejado: '))
print(f'O número base {num_base} elevado a potência {num_expoente}, tem resultado {potencia(num_base, num_expoente)}')



print('~='*20)
print('Ex: 23')
print('~='*20)

def fatorial(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * fatorial(n - 1)

num = int(input('Digite um número: '))
print(f'O fatorial de {num} é {fatorial(num)}')



print('~='*20)
print('Ex: 24')
print('~='*20)

def dobrar(num1):
  return num1 * 2
 
def quadrado(num2):
  return dobrar(num2) ** 2

usuario = int(input('Digite um numero: '))
print(f'O quadrado do dobro do número {usuario} é {quadrado(usuario)}')




print('~='*20)
print('Ex: 25')
print('~='*20)   

def cubo (num):
    return num ** 3

numero_usuario = int(input('Digite um número: '))
print(f'O cubo do número {numero_usuario} é {cubo(numero_usuario)} ')

#ou pode ser assim

cubo = lambda num:num ** 3

numero_usuario = int(input('Digite um número: '))
print(f'O cubo do número {numero_usuario} é {cubo(numero_usuario)} ')




print('~='*20)
print('Ex: 26')
print('~='*20)

def multiplicar (n1, n2):
    return n1 * n2

numero1_usuario = int(input('Digite um número: '))
numero2_usuario = int(input('Digite outro número: '))


print(f'O número {numero1_usuario} multiplicado por {numero2_usuario}, tem resultado {numero1_usuario*numero2_usuario}')

#ou pode ser assim

multi = lambda num1, num2 : num1 * num2

numero_usuario = int(input('Digite um número: '))
numero2_usuario = int(input('Digite outro número: '))


print(f'O número {numero_usuario} multiplicado por {numero2_usuario}, tem resultado {multi(numero_usuario, numero2_usuario)}')




print('~='*20)
print('Ex: 27')
print('~='*20)

def par_ou_impar(num):
    if num % 2 == 0:
        return 'Número par'
    else:
        return 'Número impar'

numero_usuario = int(input('Digite um número: '))
print(f'O número {numero_usuario} é {par_ou_impar(numero_usuario)}')

#ou pode ser assim

par_ou_impar = lambda num : 'par' if num %2 == 0 else 'impar'

numero_usuario = int(input('Digite um número: '))
print(f'O número {numero_usuario} é {par_ou_impar(numero_usuario)}')



print('~='*20)
print('Ex: 28')
print('~='*20)

numeros = [1, 2, 3, 4, 5, 6]
quadrado = lambda num : num ** 2

resultados = []
for i in numeros:
    resultados.append(quadrado(i))
print(f'Os quadrados dos números {numeros} são {resultados}')



print('~=' * 20)
print('Ex: 33')
print('~=' * 20)

from datetime import datetime


class Funcionarios:
    def __init__(self, nome, sobrenome, anoNascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.anoNascimento = anoNascimento

    def nomeCompleto(self):
        return self.nome, self.sobrenome, self.anoNascimento

    def idadeFuncionario(self):
        ano_atual = datetime.now().year
        self.anoNascimento = int(ano_atual - self.anoNascimento)
        return self.anoNascimento


usuario1 = Funcionarios('Thiago', 'Macedo', 1987)
usuario2 = Funcionarios('Roberta', 'Gualberto', 1990)

print(Funcionarios.nomeCompleto(usuario1), Funcionarios.idadeFuncionario(usuario1))
print(Funcionarios.nomeCompleto(usuario2), Funcionarios.idadeFuncionario(usuario2))


def somar():
    print('Esta funcao vai somar valores.')

def multi():
    print('Esta funcao vai multiplicar valores.')

def findIndex(to_find, item):
    for i, valor in enumerate(to_find):
        if valor == item:
            return i
    return 'Nao existe'

