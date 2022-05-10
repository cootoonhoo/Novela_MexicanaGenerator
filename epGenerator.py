from random import randint
try:
    listAcoes = open("lists/acoes.txt", "r", encoding="utf-8")
    listLocais = open("lists/locais.txt", "r", encoding="utf-8")
    listFimProtagonistas = open("lists/finais_protagonista.txt", "r", encoding="utf-8")
    listFimViloes = open("lists/finais_viloes.txt", "r", encoding="utf-8")
    openTest = True
except:
    print("Não foi possivel ler os arquivos referentes aos nomes")
    openTest = False

s = None
allAcoes = []
while(s != ""):
    s = listAcoes.readline()
    allAcoes.append(s.rstrip("\n"))
allAcoes.pop()

s = None
allLocais = []
while(s != ""):
    s = listLocais.readline()
    allLocais.append(s.rstrip("\n"))
allLocais.pop()

s = None
allFinaisProtagonistas = []
while(s != ""):
    s = listFimProtagonistas.readline()
    allFinaisProtagonistas.append(s.rstrip("\n"))
allFinaisProtagonistas.pop()

s = None
allFinaisViloes = []
while(s != ""):
    s = listFimViloes.readline()
    allFinaisViloes.append(s.rstrip("\n"))
allFinaisViloes.pop()

#Geradores
def lineGeneratorScenarioA(NomeProtagonistas, ListaCoadjuvantes):
    randomLocal = randint(0, len(allLocais) -1)
    randomAcao = randint(0, len(allAcoes) -1)
    randomCoadjuvante = randint(0, len(ListaCoadjuvantes) -1)
    RoteiroLinha = NomeProtagonistas+ " " + allAcoes[randomAcao] + " " + ListaCoadjuvantes[randomCoadjuvante] + " " + allLocais[randomLocal]
    return RoteiroLinha


def lineGeneratorScenarioB(NomeVilao, ListaPersonagens):
    randomLocal = randint(0, len(allLocais) -1)
    randomAcao = randint(0, len(allAcoes) -1)
    randomPersonagem = randint(0, len(ListaPersonagens) -1)
    RoteiroLinha = NomeVilao+ " " + allAcoes[randomAcao] + " " + ListaPersonagens[randomPersonagem] + " " + allLocais[randomLocal]
    return RoteiroLinha

def lineGeneratorScenarioC(NomeProtagonistas, ListaViloes):
    randomLocal = randint(0, len(allLocais) -1)
    randomAcao = randint(0, len(allAcoes) -1)
    randomCoadjuvante = randint(0, len(ListaViloes) -1)
    RoteiroLinha = NomeProtagonistas+ " " + allAcoes[randomAcao] + " " + ListaViloes[randomCoadjuvante] + " " + allLocais[randomLocal]
    return RoteiroLinha

def lineGeneratorScenarioD(NomeProtagonistas,ListaVilao):
    randomFinal = randint(0, len(allFinaisProtagonistas) -1)
    randomVilao = randint(0, len(ListaVilao) -1)
    RoteiroLinha = NomeProtagonistas+ " " + allFinaisProtagonistas[randomFinal]
    RoteiroLinha = RoteiroLinha.replace("#", ListaVilao[randomVilao])
    return RoteiroLinha

def lineGeneratorScenarioE(NomeVilao,ListaProtagonistas):
    randomFinal = randint(0, len(allFinaisViloes) -1)
    randomProtagonista= randint(0, len(ListaProtagonistas) -1)
    RoteiroLinha = NomeVilao+ " " + allFinaisViloes[randomFinal]
    RoteiroLinha = RoteiroLinha.replace("#", ListaProtagonistas[randomProtagonista])
    return RoteiroLinha

def renderEpisodeScenarioA(ListaProtagonistas, ListaCoadjuvantes, Arquivo):
    for i in range(len(ListaProtagonistas)):
        RoteiroLinha =lineGeneratorScenarioA(ListaProtagonistas[i], ListaCoadjuvantes)
        if(i%2 == 0):
            RoteiroLinha = RoteiroLinha.replace("@", "o")
        else:
            RoteiroLinha = RoteiroLinha.replace("@", "a")
        print(RoteiroLinha)
        Arquivo.write(RoteiroLinha+"\n")

#Renders
def renderEpisodeScenarioB(ListaVilao, ListaPersonagens, Arquivo):
    for i in range(len(ListaVilao)):
        RoteiroLinha =lineGeneratorScenarioA(ListaVilao[i], ListaPersonagens)
        if(i%2 == 0):
            RoteiroLinha = RoteiroLinha.replace("@", "o")
        else:
            RoteiroLinha = RoteiroLinha.replace("@", "a")
        print(RoteiroLinha)
        Arquivo.write(RoteiroLinha+"\n")

def renderEpisodeScenarioC(ListaProtagonistas, ListaViloes,Arquivo):
    for i in range(len(ListaProtagonistas)):
        RoteiroLinha =lineGeneratorScenarioA(ListaProtagonistas[i], ListaViloes)
        if(i%2 == 0):
            RoteiroLinha = RoteiroLinha.replace("@", "o")
        else:
            RoteiroLinha = RoteiroLinha.replace("@", "a")
        print(RoteiroLinha)
        Arquivo.write(RoteiroLinha+"\n")

def RenderFinal(ListaProtagonistas, ListaViloes, Arquivo):
    for i in range(len(ListaProtagonistas)):
        RoteiroLinha = lineGeneratorScenarioD(ListaProtagonistas[i], ListaViloes)
        if(i%2 == 0):
            RoteiroLinha = RoteiroLinha.replace("@", "o")
        else:
            RoteiroLinha = RoteiroLinha.replace("@", "a")
        print(RoteiroLinha)
        Arquivo.write(RoteiroLinha+"\n")
    for i in range(len(ListaViloes)):
        RoteiroLinha = lineGeneratorScenarioE(ListaViloes[i],ListaProtagonistas)
        if(i%2 == 0):
            RoteiroLinha = RoteiroLinha.replace("@", "o")
        else:
            RoteiroLinha = RoteiroLinha.replace("@", "a")
        print(RoteiroLinha)
        Arquivo.write(RoteiroLinha+"\n")

#Geradores de Ep
def FinalEpGenerator(PersonagensPrincipais, Viloes,Arquivo):
    RenderFinal(PersonagensPrincipais, Viloes, Arquivo)
    
def ComumEpGenerator(PersonagensPrincipais,Coadjuvantes,Viloes, Arquivo):
        renderEpisodeScenarioA(PersonagensPrincipais, Coadjuvantes, Arquivo)
        renderEpisodeScenarioB(Viloes, PersonagensPrincipais, Arquivo)
        renderEpisodeScenarioC(PersonagensPrincipais, Viloes, Arquivo)
        print()
        Arquivo.write("\n")

if (openTest):
    listAcoes.close()
    listLocais.close()
