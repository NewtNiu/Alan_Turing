# Niumar Girardi

def resumo():
    mensagem = "Alan Mathison Turing  foi um matemático britânico, pioneiro da computação e considerado o pai da ciência computacional e da inteligência artificial."
    return mensagem


def doutorado():
    mensagem = ""
    return mensagem


def contribuicoes():
    mensagem = "Alan Turing, matemático britânico, quebrou o código da máquina Enigma, usada pelos nazistas na Segunda Guerra Mundial, criando uma máquina chamada Bombe. A Enigma codificava mensagens militares usando rotores que alteravam as configurações a cada caractere digitado, tornando a cifra extremamente complexa. A Bombe de Turing simulava diversas configurações possíveis da Enigma, identificando padrões repetidos em mensagens, como saudações padrão, para reduzir o número de combinações e descobrir as configurações diárias. Após a guerra, Turing também contribuiu para a ciência da computação ao propor o Jogo da Imitação, mais conhecido como Teste de Turing. Esse teste avalia a inteligência de máquinas comparando suas respostas com as de humanos em uma interação textual. Se um avaliador não consegue distinguir as respostas da máquina das de um humano, a máquina passa no teste, sugerindo capacidade de raciocínio semelhante à humana."
    return mensagem


def artigos():
    mensagem = "Alan Turing contribuiu com artigos como On Computable Numbers (1936), que introduziu as máquinas de Turing e a base teórica da computação, A Method for the Calculation of the Zeta-Function (1939), sobre a função zeta de Riemann, Computing Machinery and Intelligence (1950), que propôs o Teste de Turing, e The Chemical Basis of Morphogenesis (1952), explicando padrões naturais por reações químicas."
    return mensagem


def citacoes():
    mensagem = "https://www.alura.com.br/artigos/decifrando-alan-turing-vida-trajetoria-tecnologia#:~:text=Considerado%20uma%20das%20mentes%20mais,o%20Enigma%20da%20inteligência%20nazista.\nhttps://brasilescola.uol.com.br/biografia/alan-mathison.htm\nhttps://www.feg.unesp.br/Home/PaginasPessoais/CristovaoCunha/ai-alan-turing.pdf"
    return mensagem


def sair():
    mensagem = "\nObrigado pela leitura!"
    return mensagem


def erro():
    mensagem = "\nOpção inválida!"
    return mensagem


print("\nBoa noite! Você está aprendendo sobre Allan Turing.\n")

continuar = True
while continuar == True:

    opcao = int(
        input(
"""
\nDigite o número correspondente ao menu que você deseja acessar:
1 - Resumo
2 - Doutorado
3 - Contribuições
4 - Principais Artigos
5 - Citações
6 - Sair\n
"""
        )
    )

    if opcao == 1:
        print("1 - Resumo")
        mensagem = resumo()

    elif opcao == 2:
        print("2 - Doutorado")
        mensagem = doutorado()

    elif opcao == 3:
        print("3 - Contribuições")
        mensagem = contribuicoes()

    elif opcao == 4:
        print("4 - Principais Artigos")
        mensagem = artigos()

    elif opcao == 5:
        print("5 - Citações")
        mensagem = citacoes()

    elif opcao == 6:
        mensagem = sair()
        continuar = False

    else:
        mensagem = erro()

    print(mensagem)
