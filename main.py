from perguntas import quest
from funcoes import *

def main():
    print("Olá! Você está na Fortuna DesSoft e terá a oportunidade de enriquecer!\n")

    nome = input("Qual seu nome? ").strip().upper()

    print(f"\nOk {nome}, você tem direito a pular 3 vezes e 2 ajudas!")
    print('As opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"!')
    input("\nAperte ENTER para continuar...\n")

    print("O jogo já vai começar! Lá vem a primeira questão!\n")

    problemas = valida_questoes(quest)

    for erro in problemas:
        if erro != {}:
            print("A base de questões está inconsistente.")
            return

    questoes = transforma_base(quest)

    print("Vamos começar com questões do nível FACIL!")
    input("Aperte ENTER para continuar...\n")

    nivel = "facil"
    questoes_sorteadas = []

    questao = sorteia_questao_inedita(questoes, nivel, questoes_sorteadas)

    print(questao_para_texto(questao, 1))

    opcoes_validas = ["A", "B", "C", "D", "ajuda", "pula", "parar"]

    resposta = input("\nQual sua resposta?! ")

    while resposta not in opcoes_validas:
        print("Opção inválida!")
        print('As opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"!\n')
        resposta = input("Qual sua resposta?! ")

    if resposta == questao["correta"]:
        print("\nVocê acertou!")
    else:
        print("\nQue pena! Você errou!")

    print(f"Você digitou: {resposta}")

if __name__ == "__main__":
    main()