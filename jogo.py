import random

print("BEM VINDO AO JOGO!!! \n")

print("Niveis de dificuldade")
print("(1) Fácil (2) Medio (3) Dificil:")

dificuldade = int(input("Escolha a dificuldade: \n"))
tentativas = 0

if(dificuldade ==1):
    tentativas = 15
elif (dificuldade == 2):
    tentativas = 10
elif(dificuldade == 3):
    tentativas = 5
else:
    print("Escoha invalida")

numero = random.randrange(1, 101)
score = 500

for turno in range(1, tentativas + 1):
    print(f"Tentativa {turno} de {tentativas}")
    bet = int(input("Digiti a o numero da aposta: "))

    if (bet < 1 or bet > 100):
        print("O numero deve estar entre 1 e 100!")
        continue

    certo = bet == numero
    maior = bet > numero
    menor = bet < numero

    if (certo):
        print(f"Você acertou e marcou {score}")
        break
    else:
        if (maior):
            print("Você errou! O seu chute foi maior .")
        elif (menor):
            print("Você errou! O seu chute foi menor.")
        pontos_perdidos = abs(numero - bet)
        score = score - pontos_perdidos

print("Fim do jogo")
