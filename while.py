num = int(input("Informe um valor inteiro e positivo: "))
while num <= 0:
    print("Erro, o valor deve ser positivo. ")
    num = int(input("Informe um valor inteiro e positivo: "))

soma = 0 
d = 1
while d < num:
    if num%d == 0: soma += d
    d += 1

if soma == num: 
    print("Número perfeito")
else:  
    print("Número não é perfeito")
