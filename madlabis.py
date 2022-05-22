#Esse projeto tem a função de explorar as formatações do print e as concatenações!
#Também tem a introdução aos operadores aritimeticos e lógicos;
#O programa ainda não esta completo, mas ja foi utilizado algumas tecnicas de formatação;

print("Olá Programador :)\n")

name = input("Digite seu nome, dev: \n") #Informe seu nome :)

idade = int(input("Qual a sua idade ?\n"))

print(f'Olá, dev {name}, é um prazer te conhecer, você tem {idade} anos.\n Lembre-se, nunca é tarde para aprender a Programar! :)\n') 
#Mensagem utiliando seu nome e idade informados!

print("Aqui está o Madlabis: \n")
print("Olá, sabia que programar é muito ___________? A programação me deixa feliz todo momento porque Eu amo programar, o mundo da Programação é tão vasto e amplo, em que podemos fazer o que quisermos. Eu adoraria ___________ bastante. Mantenha-se hidratado e ___________ e vamos assistir algum filme do ___________ ?. Eu gosto bastante de filmes, séries e jogos. Meu jogo favorito é ___________, meu filme favorito é ___________ e meu seriado favorito é ___________. Estou a todo momento escutando muitas músicas de artistas que ___________, ajudam a me acalmar e pensar melhor, principalmente quando estou programando. :D \n")

print("Agora complete os espaços em branco com as seguintes expressões: ")
adj = input("Adjetivo: ")
verb1 = input("Verbo: ")
verb2 = input("Verbo: ")
personagem_famoso = input("Personagem famoso: ")
game = input("Jogo Preferido: ")
film = input("Filme Favorito: ")
serie = input("Serie Favorita: ")
verb3 = input("Verbo: ")

print("\nAgora que você terminou, veja o resultado: \n")

madlib = f"Olá, sabia que programar é muito {adj}? A programação me deixa feliz todo momento porque Eu amo programar, o mundo da Programação é tão vasto e amplo, em que podemos fazer o que quisermos. Eu adoraria {verb1} bastante. Mantenha-se hidratado e {verb2} e vamos assistir algum filme do {personagem_famoso} ?. Eu gosto bastante de filmes, séries e jogos. Meu jogo favorito é {game}, meu filme favorito é {film} e meu seriado favorito é {serie}. Estou a todo momento escutando muitas músicas de artistas que {verb3}, ajudam a me acalmar e pensar melhor, principalmente quando estou programando :D "

print(madlib)


print("\nIsso foi muito fácil né?, mas algumas pessoas gostam passar horas e horas em Madlabis. :) ")

print ("\nAgora vamos brincar de Calculadora. Informe dois números para poder ver seus resultados: ")

num1 = float(input("Primeiro número: "))
num2 = float(input("Segundo Número: "))

print(f'Resultados:\n  {num1} + {num2} = {num1+num2} \n  {num1} - {num2} = {num1-num2} \n  {num1} * {num2} = {num1*num2} \n  {num1} / {num2} = {num1 / num2} e o seu resto {num1 % num2}')

print("Isso é tudo, obrigado por executar o meu código! :)") 