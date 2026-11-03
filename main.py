# 1. Variáveis de estado criadas antes do loop
tentativas = 3
pontos = 0


# Pergunta matemática que será feita
resposta_correta = 12  # Exemplo: 4 * 3


# 2. Loop que continua enquanto houver tentativas
while tentativas > 0:
    print(f"\Você tem {tentativas} tentativa(s) restante(s).")
   
    # 3. Input dentro do loop para receber a resposta
    resposta_jogador = int(input("Quanto é 4 vezes 3? "))
   
    # 3. Verificação com if/else
    if resposta_jogador == resposta_correta:
        # 4. Se acertar: soma 1 ponto e para o loop
        print("Parabéns! Resposta correta.")
        pontos = pontos + 1
        break  # Interrompe o while imediatamente
    else:
        # 5. Se errar: diminui 1 do contador de tentativas restantes
        tentativas = tentativas - 1
        # 5. Exibe a mensagem avisando que o jogador errou o palpite
        print("Resposta incorreta!")


# 6. Depois do loop, exibe a mensagem de encerramento do quiz
print("\--- FIM DO JOGO ---")
# 6. Mostra na tela a pontuação final obtida pelo jogador
print(f"Sua pontuação final é: {pontos} ponto(s).")

