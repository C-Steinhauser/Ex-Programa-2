import random

#Exercício 1

def transforma_base(lista_questoes):
    dic = {}
    for questao in lista_questoes:
        for inf in questao:
            if inf == "nivel":
                if questao[inf] not in dic:
                    dic[questao[inf]] = [questao]
                else:
                    dic[questao[inf]].append(questao)

    return dic

#Exercício 2

def valida_questao(questao):
    erros = {}

    chaves_obrigatorias = {"titulo", "nivel", "opcoes", "correta"}
    niveis_validos = {"facil", "medio", "dificil"}
    respostas_validas = {"A", "B", "C", "D"}

    for chave in chaves_obrigatorias:
        if chave not in questao:
            erros[chave] = "nao_encontrado"
    if len(questao) != 4:
        erros["outro"] = "numero_chaves_invalido"
    if "titulo" in questao:
        if not isinstance(questao["titulo"], str) or questao["titulo"].strip() == "":
            erros["titulo"] = "vazio"
    if "nivel" in questao:
        if questao["nivel"] not in niveis_validos:
            erros["nivel"] = "valor_errado"
    if "opcoes" in questao:
        opcoes = questao["opcoes"]
        if not isinstance(opcoes, dict) or len(opcoes) != 4:
            erros["opcoes"] = "tamanho_invalido"
        else:
            if set(opcoes.keys()) != respostas_validas:
                erros["opcoes"] = "chave_invalida_ou_nao_encontrada"
            else:
                vazias = {}
                for letra in ["A", "B", "C", "D"]:
                    if not isinstance(opcoes[letra], str) or opcoes[letra].strip() == "":
                        vazias[letra] = "vazia"

                if vazias:
                    erros["opcoes"] = vazias

    if "correta" in questao:
        if questao["correta"] not in respostas_validas:
            erros["correta"] = "valor_errado"

    return erros

#Exercício 3

def valida_questoes(lista_questoes):
    lista_erros = []

    for questao in lista_questoes:
        erros_da_questao = valida_questao(questao)
        lista_erros.append(erros_da_questao)

    return lista_erros

#Exercício 4

def sorteia_questao(questoes, nivel):
    return random.choice(questoes[nivel])

#Exercício 5

def sorteia_questao_inedita(questoes, nivel, questoes_sorteadas):
    questao = sorteia_questao(questoes, nivel)

    while questao in questoes_sorteadas:
        questao = sorteia_questao(questoes, nivel)

    questoes_sorteadas.append(questao)

    return questao

#Exercício 6

def questao_para_texto(questao, id):
    texto = "----------------------------------------\n"
    texto += f"\033[96mQUESTAO {id}\033[0m\n\n"
    texto += questao["titulo"] + "\n\n"
    texto += "RESPOSTAS:\n"
    texto += f"A: {questao['opcoes']['A']}\n"
    texto += f"B: {questao['opcoes']['B']}\n"
    texto += f"C: {questao['opcoes']['C']}\n"
    texto += f"D: {questao['opcoes']['D']}"

    return texto

#Exercício 7

def gera_ajuda(questao):
    erradas = []

    for letra in ["A", "B", "C", "D"]:
        if letra != questao["correta"]:
            erradas.append(questao["opcoes"][letra])

    quantidade = random.randint(1, 2)

    dicas = random.sample(erradas, quantidade)

    return "DICA:\nOpções certamente erradas: " + " | ".join(dicas)