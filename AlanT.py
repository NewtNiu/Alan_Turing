# Niumar Girardi
# Luiz Gustavo

def resumo():
    mensagem = "Alan Turing (1912-1954) foi um matemático britânico que revolucionou a ciência e a tecnologia. Ele é famoso por desenvolver o conceito de uma máquina teórica, a máquina de Turing, que definiu como computadores podem resolver problemas usando algoritmos. Durante a Segunda Guerra Mundial, Turing teve um papel crucial ao ajudar a decifrar os códigos da máquina Enigma, utilizada pelos nazistas, trabalho que contribuiu para encurtar a guerra e salvar milhões de vidas. Apesar de suas conquistas, ele enfrentou grande discriminação por ser homossexual, algo considerado crime na Inglaterra da época. Em 1952, foi condenado e submetido a um tratamento químico degradante. Dois anos depois, morreu em circunstâncias suspeitas, oficialmente registradas como suicídio. Hoje, é lembrado como um dos maiores gênios da história e símbolo da luta por justiça e igualdade."
    return mensagem


def doutorado():
    mensagem = "Alan Turing realizou seu doutorado na Universidade de Princeton, nos Estados Unidos, entre 1936 e 1938, sob a orientação de Alonzo Church, um renomado matemático e lógico. Durante esse período, Turing aprofundou seus estudos sobre lógica matemática e teoria da computação, expandindo as ideias apresentadas em seu artigo seminal sobre números computáveis e a máquina de Turing. Sua tese de doutorado abordou o conceito de sistemas lógicos e a noção de ordinal logics, explorando os limites da prova matemática e a relação entre sistemas formais e computabilidade. Esse trabalho foi fundamental para consolidar sua reputação como um dos principais teóricos de sua época e lançou as bases para muitas das inovações futuras em ciência da computação e inteligência artificial."
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