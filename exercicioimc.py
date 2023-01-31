nome=input('Qual é o seu nome? ')
peso=int(input('Qual o seu peso? '))
altura=float(input('Sua altura? '))
imc=peso/(altura**2)

print(nome,'tem', altura, 'de altura,', 'pesa', peso, 'quilos e seu IMC é', imc)
