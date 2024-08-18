# Criar um sistema na qual calcule o IMC 

nome = ""
altura = 0 #em metros
peso = 0. #em quilos
imc = 0. #resultado imc

def ler_dados():
    global nome
    global altura
    global peso 

    nome = input("Digite o seu nome: ")
    altura = float(input("Digite sua altura em metros: "))
    peso = int(input("Digite o seu peso em quilos: "))

def calcula_imc():
    global peso 
    global altura 

    imc = peso / pow(altura, 2) # pow eleva a altura a 2
    return round(imc, 2) #round retorna o imc com o arredondamento de duas casas decimais

def avalia_imc():
    imc = calcula_imc()
    if imc < 18.5:
        return "abaixo do peso."
    elif imc >= 18.5 and imc < 25:
        return "com o peso ideal"
    else:
        return "com Sobrepeso."
    
ler_dados()
imc = calcula_imc()
msg = avalia_imc()
print(f' {nome} está {msg}')