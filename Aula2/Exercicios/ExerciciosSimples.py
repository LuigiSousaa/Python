# Exercício 1
a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
raio = float(input("Digite o valor do raio: "))

pi = 3.14

soma =  a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
divisao_inteira = a // b
resto_divisao = a % b
potencia = a ** b
area = pi * raio**2

print(soma, subtracao, multiplicacao, divisao, divisao_inteira, resto_divisao, potencia, area)

# Exercício 2
nome = str(input("Digite seu nome: "))
sobrenome = str(input("Digite seu sobrenome: "))

nomeCompleto = nome + " " + sobrenome

print(nomeCompleto.title())

texto = "Este texto está sofrendo alterações"

textoMaiusculo = texto.upper() # texto maiúsculo
textoMinusculo = texto.lower() # texto minúsculo

texto_substituido = texto.replace("texto", "maluco") # texto substituindo palavra
quantidadePalavras = len(texto.split()) # quantas palavras

print(f"Texto maiúsculo: {textoMaiusculo}")
print(f"Texto minúsculo: {textoMinusculo}")
print(f"Texto substituído: {texto_substituido}")
print(f"Quantidade de palavras: {quantidadePalavras}")

#Exercício 3
lista_cores = ["vermelho", "azul", "amarelo"]
print(lista_cores)
lista_cores.append(str(input("Adicione uma cor: ")))
print(lista_cores)

lista_coordenadas = (int(input("Insira o valor da logitude: ")), int(input("Insira o valor da latitude: ")))

longitude, latitude = lista_coordenadas
print("Longitude: ", longitude)
print("Latitude: ", latitude)

#Exercício 4

temSol = boolean(input("Há sol? [S/N]: ")).lower() == 's'
temChuva = boolean(input("Está chovendo? [S/N]: ")).lower() == 's'

if temSol and not temChuva:
    print("O clima está agradável")
elif not temSol and temChuva:
    print("O clima está feio")
