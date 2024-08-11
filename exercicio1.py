# exercicio 1: escrever um programinha que leia 4 notas de um aluno e calcular a media das notas 


name = input("Qual é o seu nome? ")

print(f"Então {name}, seja bem vindo ao nosso sistemas de notas e para isso precisaremos das 4 notas que você tirou em Inglês para fazer a média do 7")

nota1 = int(input("Insira a sua primeira nota: "))
nota2 = int(input("Insira a sua segunda nota: "))
nota3 = int(input("Insira a sua terceira nota: "))
nota4 = int(input("Insira a sua quarta nota: "))

resultadodamedia = (nota1 + nota2 + nota3 + nota4) / 4

if resultadodamedia > 6: 
    print(f"Parabéns {name}! Você foi aprovado no nosso bimestre! Aqui está a sua média das notas: {resultadodamedia}")
else: 
    print(f"Infelizmente {name}, você foi reprovado no nosso bimestre. A sua média das notas foi {resultadodamedia}")