# strings

gameName = "hollow knight"
gameName2 = "Hollow Knight"
gameDescription = "Hollow Knight é um jogo indie de gênero metroidvania desenvolvido e publicado pela Team Cherry, lançado para Microsoft Windows, macOS e Linux em 2017 e, posteriormente, para Nintendo Switch, Playstation 4 e Xbox One em 2018 "
gameAno = "2018"

print(gameName) # hollow knight
print(gameName2) # Hollow Knight
print(gameName == gameName2) # case senstive, false
print(gameName == gameName) #true
print(gameName.upper() == gameName2.upper()) # true

# operações com strings


print(gameName + gameAno) # hollow knight2018
print(f'{gameName} foi feito em {gameAno}') # hollow knight foi feito em 2018 

# operando multiplicação de strings. 

line = "="
print(line * 25) # *************************

# buscando uma palavra no texto 

print("2018" in gameDescription) # true
print("hollow knight" in gameDescription) # false


# fatiar strings, famoso slice 
# string loop, string[indice:fim] - indice começa na posição 1 | indice final -1 

# 1 buscar toda string a partir da primeira pos 

# obs: 0 que começa como 1, e serve como array. exemplo, hollow knight = ["h","o", "l", "l", "o","w", "k","n","i","g","h","t"]
# setou o 0 como primeiro indice, vai buscar hollow knight. se setou indice 5 vai buscar w knight


print(gameName[0:]) # hollow knight 
print (gameName[7:]) # knight. ps: se fosse 6, ia juntar com espaço junto. então ele conta com os espaços junto também. 


# 2 buscar todas string até a ultima posição 

print(gameName[0:6]) # hollow 


# 3 buscar toda string de 2 em 2 caracteres 

#hollow knight

print(gameName[::2]) #hlo ngt

# buscar toda string nos indices impares

print(gameName[1::2]) # olwkih

# inverter uma string de trás pra frente 

print(gameName[::-1]) #thgink wolloh



# principais métodos do string

print(gameName.upper()) # retorna string inteira em maiusculo 
print(gameName.lower()) # retorna string inteira em minusculo
print(gameName.capitalize()) # apenas primeira letra do string fica em maisculo 
print(gameName.title()) # faz a mesma função do capitalize. 
# hollow knight
print(len(gameName)) # 13, conta quanto numeros tem na string
print(gameName.center(16, '-')) # -hollow knight--, retorna string centralizada com caractere de preenchimento 
print(gameName.find('l')) # conta quantos numeros iguais tem 
 
# e mto mais... 




