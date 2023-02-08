#Elabore um programa que
#solicita: nome, endereço, CEP e
#telefone. Imprima na tela os
#valores conforme abaixo:
#nome na primeira linha,
#endereço na segunda linha,
#CEP e telefone na terceira linha.

n=str(input("Digite seu nome: "))
end=str(input("Digite seu endereço: "))
cep=int(input("Digite seu CPF (Sem pontos ou traços): "))
tel=int(input("Digite seu telefone: "))

print("Nome: ",n,"\nEndereço: ",end,"\nCep: ",cep," Telefone:", tel)


