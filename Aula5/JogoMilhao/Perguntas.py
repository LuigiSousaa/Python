def perguntasFaceis():
    listaFacil = [
        {
            "pergunta": "Limeira é conhecida como capital da(o):",
            "alternativas": ["a)Laranja", "b)Jóia", "c)Café", "d)TI"],
            "resposta": "b)",
        },
        {
            "pergunta": "Quem era o escrivão da expedição de Pedro Álvares Cabral?",
            "alternativas": [
                "a)Dom Pedro I",
                "b)Dom Pedro II",
                "c)Pedro Vaz de Caminha",
                "d)Pero Vaz de Caminha",
            ],
            "resposta": "d)",
        },
        {
            "pergunta": "Quantos graus há em um ângulo reto?",
            "alternativas": [
                "a)20 graus",
                "b)60 graus",
                "c)90 graus",
                "d)180 graus",
            ],
            "resposta": "c)",
        },
    ]
    return listaFacil  # Quando a função é executada, a lista é criada, mas não está disponível fora da função. Portanto, qualquer tentativa de acessar listaFacil fora da função resultaria em um erro, já que a variável não está definida.
