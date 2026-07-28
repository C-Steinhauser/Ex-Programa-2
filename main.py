from perguntas import quest
from funcoes import *

VERMELHO = "\033[91m"
VERDE = "\033[92m"
AMARELO = "\033[93m"
AZUL = "\033[94m"
CIANO = "\033[96m"
ROXO = "\033[95m"
NEGRITO = "\033[1m"
RESET = "\033[0m"


def jogar():
    print(f"{CIANO}Olá! Você está na Fortuna DesSoft e terá a oportunidade de enriquecer!{RESET}\n")

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

    nivel = "facil"
    questoes_sorteadas = []
    premios = [1000, 5000, 10000, 30000, 50000, 100000, 300000, 500000, 1000000]
    indice_premio = 0
    premio_atual = 0
    numero_questao = 1
    pulos = 3
    ajudas = 2

    print("Vamos começar com questões do nível FACIL!")
    input("Aperte ENTER para continuar...\n")

    while True:
        questao = sorteia_questao_inedita(questoes, nivel, questoes_sorteadas)
        ajuda_usada_nesta_questao = False

        print(questao_para_texto(questao, numero_questao))

        while True:
            opcoes_validas = ["A", "B", "C", "D", "ajuda", "pula", "parar"]
            resposta = input("\nQual sua resposta?! ").strip()

            while resposta not in opcoes_validas:
                print(f"{AMARELO}Opção inválida!{RESET}")
                print('As opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"!\n')
                resposta = input("Qual sua resposta?! ").strip()

            if resposta in ["A", "B", "C", "D"]:
                if resposta == questao["correta"]:
                    premio_atual = premios[indice_premio]
                    indice_premio += 1

                    print(f"\n{VERDE}Você acertou! Seu prêmio atual é de R$ {premio_atual:.2f}{RESET}")

                    if indice_premio == len(premios):
                        print(f"\n{VERDE}{NEGRITO}PARABÉNS, você zerou o jogo e ganhou UM MILHÃO DE REAIS!!{RESET}")
                        return

                    if indice_premio == 3:
                        nivel = "medio"
                        print(f"\n{ROXO}HEY! Você passou para o nível MEDIO!{RESET}")
                    elif indice_premio == 6:
                        nivel = "dificil"
                        print(f"\n{ROXO}HEY! Você passou para o nível DIFICIL!{RESET}")

                    input("Aperte ENTER para continuar...\n")
                    numero_questao += 1
                    break
                else:
                    print(f"\n{VERMELHO}Que pena! Você errou e vai sair sem nada :({RESET}")
                    return

            elif resposta == "ajuda":
                if ajudas == 0:
                    print("Não deu! Você não tem mais direito a ajudas!")
                    input("Aperte ENTER para continuar...\n")
                    print(questao_para_texto(questao, numero_questao))
                    continue

                if ajuda_usada_nesta_questao:
                    print("Não deu! Você já pediu ajuda nesta questão!")
                    input("Aperte ENTER para continuar...\n")
                    print(questao_para_texto(questao, numero_questao))
                    continue

                ajudas -= 1
                ajuda_usada_nesta_questao = True

                if ajudas == 0:
                    print("Ok, lá vem ajuda! ATENÇÃO: Você não tem mais direito a ajudas!")
                elif ajudas == 1:
                    print("Ok, lá vem ajuda! Você ainda tem 1 ajuda!")
                else:
                    print(f"Ok, lá vem ajuda! Você ainda tem {ajudas} ajudas!")

                input("Aperte ENTER para continuar...\n")
                print(f"{AZUL}{gera_ajuda(questao)}{RESET}")
                input("Aperte ENTER para continuar...\n")
                print(questao_para_texto(questao, numero_questao))

            elif resposta == "pula":
                if pulos == 0:
                    print("Não deu! Você não tem mais direito a pulos!")
                    input("Aperte ENTER para continuar...\n")
                    print(questao_para_texto(questao, numero_questao))
                    continue

                pulos -= 1

                if pulos == 0:
                    print("Ok, pulando! ATENÇÃO: Você não tem mais direito a pulos!")
                elif pulos == 1:
                    print("Ok, pulando! Você ainda tem 1 pulo!")
                else:
                    print(f"Ok, pulando! Você ainda tem {pulos} pulos!")

                input("Aperte ENTER para continuar...\n")
                break

            elif resposta == "parar":
                if indice_premio == 0:
                    print("Você ainda não possui prêmio para retirar!")
                    input("Aperte ENTER para continuar...\n")
                    print(questao_para_texto(questao, numero_questao))
                    continue

                confirmacao = input(
                    f'Deseja mesmo parar [S/N]?? Caso responda "S", sairá com R$ {premio_atual:.2f}! '
                ).strip().upper()

                while confirmacao not in ["S", "N"]:
                    print(f"{AMARELO}Opção inválida!{RESET}")
                    confirmacao = input(
                        f'Deseja mesmo parar [S/N]?? Caso responda "S", sairá com R$ {premio_atual:.2f}! '
                    ).strip().upper()

                if confirmacao == "S":
                    print(f"\nOk! Você parou e seu prêmio é de R$ {premio_atual:.2f}")
                    return

                input("Aperte ENTER para continuar...\n")
                print(questao_para_texto(questao, numero_questao))


def main():
    while True:
        jogar()

        novamente = input("\nDeseja jogar novamente? [S/N] ").strip().upper()
        while novamente not in ["S", "N"]:
            print(f"{AMARELO}Opção inválida!{RESET}")
            novamente = input("Deseja jogar novamente? [S/N] ").strip().upper()

        if novamente == "N":
            break


if __name__ == "__main__":
    main()