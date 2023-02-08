n1=float(input("Digite a primeira nota: "))
n2=float(input("Digite a segunda nota: "))
n3=float(input("Digite a terceira nota: "))
me=float(input("Digite a média dos exercícios realizados: "))

ma = (n1 + n2*2 + n3*3 + me)/7

if ma >= 9:
    print("Parabéns, sua nota foi maior do que 9")
    print("Nota: ",round(ma,2))
elif ma< 4:
    print("Reprovado, sua nota foi menor do que 4")
    print("Nota: ",round(ma,2))
else:
    print("Sua nota foi: ",round(ma,2))