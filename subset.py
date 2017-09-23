'''
Subcadeia da soma maxima
----------------------------

Dado um conjunto de numeros, descobrir o subconjunto em que a soma dos elementos sao de maxima soma.

Exemplo: dado o conjunto de elementos [2, -4, 6, 8, -10, 100, -6, 5]

O subconjunto de soma maxima e: [2, -4, **6, 8, -10, 100**, -6, 5]

Assim, o programa deve retornar a posicao do primeiro e do ultimo elemento da subcadeia. Neste exemplo, as posicoes 2 e 5, considerando a primeira posicao com indice 0.
'''

def soma(indexa, indexb, list):
    '''
    soma: function to sum a range of list
    '''
    sum = 0
    for i in range(indexa, indexb + 1):
        sum += list[i]

    return sum


def main():
    list = [2, -4, 6, 8, -10, 100, -6, 5]
    items = dict()

    #logic to create all possbile ranges
    for i in range(0, len(list)):
        for j in range(i+1, len(list)):
            items[str(i) + " - " + str(j)]  = soma(i, j, list)


    maximum = max(items, key=items.get)
    print "The maximum value is: ", items[maximum], "- with index between", maximum


if __name__ == "__main__":
    main()
