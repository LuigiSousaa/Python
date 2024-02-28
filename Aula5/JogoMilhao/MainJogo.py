from Perguntas import perguntasFaceis
import random

# Armazena a função numa variável
listaFacil = perguntasFaceis()

# Embaralhando as perguntas (shuffle embaralha os itens da lista)
random.shuffle(listaFacil)

i = 1
for perguntaF in listaFacil:
    print(f"Pergunta {i}: " + perguntaF["pergunta"])
    print("Alternativas: ")
    for alternativaF in perguntaF["alternativas"]:
        print(alternativaF)
i += 1
