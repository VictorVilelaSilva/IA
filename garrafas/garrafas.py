from collections import deque


def resolver_enigma_garrafas(capacidade1, capacidade2, configuracao_desejada):
    fila = []
    visitados = []
    resultado = []

    # Representação do estado: (garrafa_1, garrafa_2)
    estado_inicial = (0, 0)
    fila.append(estado_inicial)
    visitados.append(estado_inicial)

    while fila:
        
        estado_atual = fila[-1]
        fila.pop()

        # Verificar se o estado atual corresponde à configuração desejada
        if estado_atual == configuracao_desejada:
            resultado = fila
            resultado.append(estado_atual)
            print(resultado)
            return True  # Enigma resolvido!

        garrafa_1, garrafa_2 = estado_atual

        # Gerar novos estados possíveis a partir das ações
        novos_estados = []

        # Ação: Encher garrafa 1
        if(garrafa_1 != capacidade1):
            novo_estado = (capacidade1, garrafa_2)
            novos_estados.append(novo_estado)

        # Ação: Encher garrafa 2
        if(garrafa_2 != capacidade2):
            novo_estado = (garrafa_1, capacidade2)
            novos_estados.append(novo_estado)

        # Ação: Esvaziar garrafa 1
        if (garrafa_1 != 0):
            novo_estado = (0, garrafa_2)
            novos_estados.append(novo_estado)

        # Ação: Esvaziar garrafa 2
        if (garrafa_2 != 0):
            novo_estado = (garrafa_1, 0)
            novos_estados.append(novo_estado)

        # Ação: Transferir conteúdo de garrafa 1 para garrafa 2
        if(garrafa_1 > capacidade2 or (garrafa_1 + garrafa_2) > capacidade2):
            temp = capacidade2 - garrafa_2
            novo_estado = [garrafa_1 - temp, capacidade2]
        else:
            novo_estado = [0, garrafa_1 + garrafa_2]
        novos_estados.append(novo_estado)

        # Ação: Transferir conteúdo de garrafa 2 para garrafa 1
        if((garrafa_1 + garrafa_2) > capacidade1):
            temp = capacidade1 - garrafa_1
            novo_estado = [capacidade1, garrafa_2 - temp]
        else:
            novo_estado = [garrafa_1 + garrafa_2, 0]
        novos_estados.append(novo_estado)

        # Verificar se os novos estados já foram visitados
        for novo_estado in novos_estados:
            if novo_estado not in visitados:
                fila.append(novo_estado)
                visitados.append(novo_estado)

    return False  # Enigma não resolvido


# Exemplo de uso:
capacidade_garrafa1 = 7
capacidade_garrafa2 = 5
configuracao_desejada = [3, 5]
print("Capacidade da garrafa1:"+str(capacidade_garrafa1))
print("Capacidade da garrafa2:"+str(capacidade_garrafa2))
print("configuração que desejamos chegar"+ str(configuracao_desejada))

if resolver_enigma_garrafas(capacidade_garrafa1, capacidade_garrafa2, configuracao_desejada):
    print("O enigma foi resolvido!")
else:
    print("O enigma não foi resolvido.")
