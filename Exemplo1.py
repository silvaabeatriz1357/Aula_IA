nota1 = float(input("digite a primeira nota:"))
nota2 = float(input("digite a segunda nota:"))
frequencia = float(input("digite a frequencia:"))

media = (nota1 + nota2)/2
print("A média é", media)

if media >= 6 and frequencia >= 75:
    print("o aluno esta aprovado !")
    print("ja pode curtir as ferias")
elif media >= 2:
    print("o aluno esta de exame !")
    print("precisa estudar mais um pouco. ")

else:
    print("o aluno esta reprovado !")
    print("nao ha direito a exame")  