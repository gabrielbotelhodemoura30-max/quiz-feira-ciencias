pontos = 0
acertos = 0

perguntas = ["Quanto é 7 + 8?", "Qual é a capital do Brasil?", "Quantas horas tem um dia?"]
respostas = ["15", "Brasilia", "24"]

for i in range(3):
    resposta = input(perguntas[i])
    if resposta == respostas[i]:
        pontos += 1
        acertos += 1
        print('Resposta correta!')
    else:
        print('Resposta errada!')

print(f'Pontuação final: {pontos}. Você acertou {acertos} perguntas...')