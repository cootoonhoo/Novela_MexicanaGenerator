import names
import epGenerator
#Variáveis importantes
PersonagensPrincipais = []
Viloes =[]
Coadjuvantes = []

#Funções
#Inputs
def inputMainCharacters():
    qntPP = int(input("Quantos PROTAGONISTAS terão em na sua novela?(Numero Par)"))
    if(qntPP%2 != 0):
        print("Erro: Numero de personagem impar")
        inputMainCharacters()
    for i in range(int(qntPP/2)):
        PersonagensPrincipais.append(names.CharacterGenerator(genFem= False))
        PersonagensPrincipais.append(names.CharacterGenerator(genFem= True))

def inputViloes():
    qntPP = int(input("Quantos VILÕES terão em na sua novela?(Numero Par)"))
    if(qntPP%2 != 0):
        print("Erro: Numero de personagem impar")
        inputViloes()
    for i in range(int(qntPP/2)):
        Viloes.append(names.CharacterGenerator(genFem= False))
        Viloes.append(names.CharacterGenerator(genFem= True))

def inputCoadjuvantes():
    qntPP = int(input("Quantos COADJUVANTES terão em na sua novela?(Numero Par)"))
    if(qntPP%2 != 0):
        print("Erro: Numero de personagem impar")
        inputCoadjuvantes()
    for i in range(int(qntPP/2)):
        Coadjuvantes.append(names.CharacterGenerator(genFem= False))
        Coadjuvantes.append(names.CharacterGenerator(genFem= True))

def inputNomeNovela():
    aux = str(input("Qual será o nome da sua novela?"))
    aux = aux.upper()
    return aux

def inputQntEp():
    return int(input("Quantos eps terá sua novela?"))
#Renders
def renderPrincipais(Arquivo):
    print()
    print("Protagonitas")
    print("=============")
    Arquivo.write("\n")
    Arquivo.write("Protagonitas\n")
    Arquivo.write("=============\n")
    for i in range(len(PersonagensPrincipais)):
        print(PersonagensPrincipais[i])
        Arquivo.write(PersonagensPrincipais[i]+ "\n")

def renderViloes(Arquivo):
    print()
    print("Viloes")
    print("======")
    Arquivo.write("\n")
    Arquivo.write("Viloes\n")
    Arquivo.write("======\n")
    for i in range(len(Viloes)):
        print(Viloes[i])
        Arquivo.write(Viloes[i]+"\n")

def renderCoadjuvantes(Arquivo):
    print()
    print("Coadjuvantes")
    print("============")
    Arquivo.write("\n")
    Arquivo.write("Coadjuvantes\n")
    Arquivo.write("============\n")
    for i in range(len(Coadjuvantes)):
        print(Coadjuvantes[i])
        Arquivo.write(Coadjuvantes[i]+"\n")

def renderNomeNovela(Arquivo):
    print()
    print("*** Novela " + NomeNovela + " ***")
    Arquivo.write("*** Novela " + NomeNovela + " ***\n")

def renderEpisode(Arquivo):
    print()
    Arquivo.write("\n")
    for i in range(QntEp - 1):
        print("Episódio " + str(i+1))
        print("============")
        print()
        Arquivo.write("Episódio " + str(i+1) + "\n")
        Arquivo.write("============\n")
        Arquivo.write("\n")
        epGenerator.ComumEpGenerator(PersonagensPrincipais, Coadjuvantes, Viloes, Arquivo)
    print("Episódio FINAL")
    print("==============")
    print()
    Arquivo.write("Episódio FINAL\n")
    Arquivo.write("==============\n")
    Arquivo.write("\n")
    epGenerator.FinalEpGenerator(PersonagensPrincipais, Viloes,Arquivo)

#Parte dos Inputs
inputMainCharacters()
inputViloes()
inputCoadjuvantes()
NomeNovela = inputNomeNovela()
QntEp = inputQntEp()

NomeArq = NomeNovela.lower()
NomeArq = NomeArq.title()

#Criando o arquivo
Arquivo = open("Resenha de " + NomeArq +".txt", "w", encoding="utf-8")
#Setor de render
renderNomeNovela(Arquivo)
renderPrincipais(Arquivo)
renderViloes(Arquivo)
renderCoadjuvantes(Arquivo)
renderEpisode(Arquivo)
print()
print("===")
print("Arquivo <"+"Resenha de " + NomeArq +".txt> salvo com sucesso!")
Arquivo.close()