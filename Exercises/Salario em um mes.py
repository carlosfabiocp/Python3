print("Esse programa irá calcular, com base nas horas trabalhadas, o salário no final do mês.")
hora = int(input("Quantas horas você trabalha por mês? "))
porhora = int(input("Quanto você ganha por hora? "))
salario = float((porhora*hora)+1000)
print("Seu salário nesse mês foi de: R${}".format(salario))