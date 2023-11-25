def getInvCount(arr):
	inv_count = 0
	empty_value = -1
	for i in range(0, 9):
		for j in range(i + 1, 9):
			if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
				inv_count += 1
	return inv_count

	
def temSolucao(puzzle) :

	# Count inversions in given 8 puzzle
	inv_count = getInvCount([j for sub in puzzle for j in sub])

	# return true if inversion count is even.
	return (inv_count % 2 == 0)

def move(tab_original):
    """
    Checa possíveis movimentos (os nós)
    da árvore
    """
    movimentos = []
    tab = eval(tab_original)
    i = 0
    j = 0
    while 0 not in tab[i]: i += 1
    j = tab[i].index(0)
    

    if i<2:         #mover o 0 para baixo 
        tab[i][j], tab[i+1][j] = tab[i+1][j], tab[i][j] 
        movimentos.append(str(tab))
        tab[i][j], tab[i+1][j] = tab[i+1][j], tab[i][j]

    if i>0:         #mover o 0 para cima
        tab[i][j], tab[i-1][j] = tab[i-1][j], tab[i][j]  
        movimentos.append(str(tab))
        tab[i][j], tab[i-1][j] = tab[i-1][j], tab[i][j]  

    if j<2:         #mover o 0 para a direita
        tab[i][j], tab[i][j+1] = tab[i][j+1], tab[i][j] 
        movimentos.append(str(tab))
        tab[i][j], tab[i][j+1] = tab[i][j+1], tab[i][j]
    
    if j>0:         #mover o 0 para a esquerda
        tab[i][j], tab[i][j-1] = tab[i][j-1], tab[i][j] 
        movimentos.append(str(tab))
        tab[i][j], tab[i][j-1] = tab[i][j-1], tab[i][j]

    return movimentos


def idfs(start,end):
    """
    Usa busca em largura para 
    resolver o quebra-cabeça
    """
    explorado = []
    banco = [[start]]
    while banco:
        i = 0
        caminho = banco[i]
        banco = banco[:i] + banco[i+1:]
        final = caminho[-1]
        if final in explorado: 
            continue
        for movimento in move(final):
            if movimento in explorado:
                continue
            banco.append(caminho + [movimento])
        explorado.append(final)
        if final == end: break
    return caminho


def h_misplaced(tabuleiro):
    """
    Implementa a heurística de 
    checar quantas peças estão 
    fora do lugar
    """
    misplaced = 0
    comparador = 1
    tab = eval(tabuleiro)
    for i in range(0,3):
        for j in range(0,3):
            if tab[i][j] != comparador:
                misplaced += 1
            comparador += 1
    return misplaced

def a_estrela(start,end):
    """
    Usa o A* para resolver
    o quebra-cabeça
    """
    explorado = []
    banco = [[h_misplaced(start),start]]
    
    while banco:
        i = 0
        for j in range(1,len(banco)):
            if (banco[i][0]) > (banco[j][0]):
               i = j
        caminho = banco[i]
        banco = banco[:i] + banco[i+1:]
        final = caminho[-1]
        if final in explorado: continue
        for movimento in move(final):
            if movimento in explorado: continue
            custo = len(caminho)-2
            novo = [(caminho[0] + h_misplaced(movimento) + h_misplaced(final)) + custo] + caminho[1:] + [movimento] 
            banco.append(novo)
        explorado.append(final)
        if final == end:
            print(custo)
            break
    return caminho



tabuleiro = str([
                [4,3,6],
                [8,7,1],
                [0,5,2]
            ])

obj_final = str([
                [1,2,3],
                [4,5,6],
                [7,8,0]
            ])


print("Usando A*:")
a=[]

if(temSolucao(eval(tabuleiro))):
    print("Tem solução")
    for i in a_estrela(tabuleiro,obj_final):
        a.append(i)
    for j in range(1,len(a)):
      print(a[j:j+1][0:11][0][0:11])
      print(a[j:j+1][0:11][0][11:22])
      print(a[j:j+1][0:11][0][22:44])
      print(str(j) + "--------------")

else :
  print("Não tem solução")


print("Usando Busca em Largura:")
if(temSolucao(eval(tabuleiro))):
    print("Tem solução")
    for i in idfs(tabuleiro,obj_final):
        a.append(i)
    for j in range(1,len(a)):
      print(a[j:j+1][0:11][0][0:11])
      print(a[j:j+1][0:11][0][11:22])
      print(a[j:j+1][0:11][0][22:44])
      print(str(j) + "--------------")

else :
  print("Não tem solução")




