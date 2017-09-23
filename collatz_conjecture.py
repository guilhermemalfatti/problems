"""
Start with a positive number n and repeatedly apply these simple rules:

If n = 1, stop.
If n is even, divide n by 2.
If n is odd, multiply n by 3 and add 1.
In 1937, Lothar Collatz asked whether this procedure always stops for every positive starting value of n. If Gerhard Opfer is correct, we can finally say that indeed it always stops.


----------------------
Conjectura de Collatz
----------------------

fonte: http://en.wikipedia.org/wiki/Collatz_conjecture

A seguinte sequência iterativa é definida pelo conjunto de inteiros positivos onde:

n -> n/2 (se n é par) n -> 3n + 1 (se n é impar)

Usando as regras acima e começando pelo número 13, nós geraríamos a seguinte sequência:

13 40 20 10 5 16 8 4 2 1

O que pode ser observado dessa sequência (começando no 13 e terminando no 1) é que ela contém 10 items. Embora ainda não esteja matematicamente provado, é esperando que, dado um numero inteiro positivo qualquer, a sequencia sempre chegará em 1.

Pergunta: Qual inteiro positivo abaixo de 1 milhão, produz a sequencia com mais items?

Desafio: Crie um código em uma das linguaguens disponíveis que calcule a resposta.

"""

class Collatz_conjecture:
    """
    This class is responsible for handling the Collatz Conjecture
    """
    def __init__(self):
        """
        Starts a Collatz_conjecture instance
        """
        self.items = []

    def sequence (self, number):
        '''
        sequence: method responsible for calculating the sequence recursively, for a number
        '''
        self.items.append(number)
        #in order to identify the the sequence of number 1, need calculate the sequence as well
        if number == 1 and len(self.items) != 1:
            return

        if number % 2 == 0:
            self.sequence(number / 2)
        else:
            self.sequence(3 * number + 1)

    def sequenceSize(self):
        '''
        sequenceSize: method responsible for returning how much items of a sequence
        '''

        return len(self.items)

    def clearSequence(self):
        '''
        clearSequence: method responsible for clear the list
        '''
        del self.items[:]



def main():
    greaterSequence = dict()
    conjecture = Collatz_conjecture()

    for i in range (1, 1000000):
        conjecture.sequence(i)
        greaterSequence[i] = conjecture.sequenceSize()
        conjecture.clearSequence()


    maximum = max(greaterSequence, key=greaterSequence.get)
    print "The maximum integer between 0 to 1000000 is: ", maximum
    print greaterSequence[maximum]


if __name__ == "__main__":
    main()