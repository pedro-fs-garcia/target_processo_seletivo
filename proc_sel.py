# exercicio 1
def fibonacci(n:int) -> bool:
    first, second = 0, 1
    if n < 0:
        print(f"O número {n} não pertence à sequência.")
        return False
    
    while second < n:
        first, second = second, first + second

    if n == first or n == second:
        print(f"O número {n} pertence à sequência.")
        return True
    else:
        print(f"O número {n} não pertence à sequência.")
        return False


# exercicio 2
def ver_a(string:str):
    count = 0
    for i in string.lower():
        if i == "a":
            count += 1
    print(f"A letra 'a' ocorrer {count} vezes na string {string}")


# exercicio 3
def exercicio_tres():
    indice = 12
    soma = 0
    k = 1
    while k < indice:
        k += 1
        soma += k
    print(soma)
    ## resultado final da soma: 77

# exercicio 4
# 4)
#    a) 9
#    b) 128
#    c) 49
#    d) 100
#    e) 13
#    f) 200


# exercicio 5
# 5) 

# Para descobrir a correspondência entre lâmpada e interruptor
# Eu ligaria o primeiro interruptor por um longo tempo (10 minutos) e o apagaria
# Imediatamente, deixaria o segundo interruptor ligado
# E iria para a primeira sala com a lâmpada. Se a lâmpada estiver acesa, ela corresponde ao segundo interruptor. Se ela estiver apagada, ela corresponde ao primeiro ou ao terceiro.
# A análise da lâmpada termina ao verificar sua temperatura. Se ela estiver quente, corresponde ao primeiro interruptor, que eu deuxei ligado por um longo tempo. Se não, corresponde ao terceiro.
# Da mesma forma faria a análise da segunda sala com lâmpada
# Ao descobrir quais as correnpondências das duas primeiras lâmpadas, a terceirta só terá uma possibilidade
