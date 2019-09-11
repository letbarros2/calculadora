print("Calculadora simples")

num1 = float(input("Insira o primeiro numero: "))
num2 = float(input("Insira o segundo numero: "))
soma=num1+num2
subtrai=num1-num2
multiplicacao=num1*num2
def divide (a,b):
    if b==0:
        print("o divisor não pode ser 0, execute novamente com outro valor")
    else:
        print("o resultado da divisao é ",(a/b))

print("o resultado da soma dos números de %d com %d é %d."%(num1,num2,soma))
print("o resulado da subtração dos números de %d com %d é %d."%(num1,num2,subtrai))
print("o resultado da multiplicação dos números  de %d com %d é %d."%(num1,num2,multiplicacao))
                                                                      
divide(num1,num2)
