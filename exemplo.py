def bubble_sort(lista):
    n = len(lista)
    for i in range(0, n - 1):
        for j in range(0, n - 1 - i):
            if lista[j] > lista[j + 1]:             # compara itens
                aux = lista[j]                      # realiza a troca
                lista[j] = lista[j + 1]
                lista[j + 1] = aux


def selection_sort(lista):
    n = len(lista)
    for i in range(0, n - 1):
        menor = i
        for j in range(i + 1, n):                   # encontra menor item
            if lista[j] < lista[menor]:
                menor = j
        aux = lista[i]                              # realiza a troca
        lista[i] = lista[menor]
        lista[menor] = aux


def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        j = i
        while j > 0 and lista[j] < lista[j - 1]:    # compara itens
            aux = lista[j]                          # realiza a troca
            lista[j] = lista[j - 1]
            lista[j - 1] = aux
            j -= 1


# -------------------------------------------------
lista = [6, 7, 4, 1, 3, 2, 5]
bubble_sort(lista)
# print(lista)

lista = [6, 7, 4, 1, 3, 2, 5]
selection_sort(lista)
# print(lista)

lista = [6, 7, 4, 1, 3, 2, 5]
insertion_sort(lista)
# print(lista)


# -------------------------------------------------
"""
EXERCÍCIO 1:
Preencha uma lista com 1000 números inteiros em ordem CRESCENTE.
Ordene a lista utilizando os métodos bubble, selection e insertion sort.
Informe para cada método:
A quantidade de operações de comparações entre elementos.
A quantidade de operações de trocas entre elementos.
"""

lista1 = list(range(1, 1001))

# Bubble Sort

n = len(lista1)

qnt_comparac, qnt_trocas = 0, 0

for i in range(0, n - 1):
    for j in range(0, n - 1 - i):
        qnt_comparac += 1
        if lista1[j] > lista1[j + 1]:
            aux = lista1[j]
            lista[j] = lista[j + 1]
            lista[j + 1] = aux
            qnt_trocas += 1

print(f'Quantidade de comparações: {qnt_comparac}, quantidade de trocas: {qnt_trocas}')



# -------------------------------------------------
"""
EXERCÍCIO 2:
Preencha uma lista com 1000 números inteiros em ordem DECRESCENTE.
Ordene a lista utilizando os métodos bubble, selection e insertion sort.
Informe para cada método:
A quantidade de operações de comparações entre elementos.
A quantidade de operações de trocas entre elementos.
"""
