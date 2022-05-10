from random import randint

# Abertura do arquivo
try:
    listNamesMasc = open("lists/nomes_masculinos.txt", "r", encoding="utf-8") 
    listNamesFem = open("lists/nomes_femininos.txt", "r", encoding="utf-8") 
    listNamesSbr = open("lists/sobrenomes.txt", "r", encoding="utf-8")
    openTest = True
except:
    print("Não foi possivel ler os arquivos referentes aos nomes")
    openTest = False

#Listagem dos nomes dentro de um vetor
#Nomes Masculinos
s = None
allNamesMasc = []
while(s != ""):
    s = listNamesMasc.readline()
    allNamesMasc.append(s.rstrip("\n"))
allNamesMasc.pop()
""" print("Lista de nomes masculinos")
print(allNamesMasc)
print() """

#Nomes Femininos
s = None
allNamesFem = []
while(s != ""):
    s = listNamesFem.readline()
    allNamesFem.append(s.rstrip("\n"))
allNamesFem.pop()
""" print("Lista de nomes femininos")
print(allNamesFem)
print() """

#Sobrenomes
s = None
allNamesSbr = []
while(s != ""):
    s = listNamesSbr.readline()
    allNamesSbr.append(s.rstrip("\n"))
allNamesSbr.pop()
""" print("Lista de sobrenomes")
print(allNamesSbr)
print() """

#Geração de personagem
def CharacterGenerator(genFem):
    FirstNameMasc = randint(0, len(allNamesMasc) - 1)
    FirstNameFem = randint(0, len(allNamesFem) - 1)
    LastName = randint(0,len(allNamesSbr) - 1)
    if (len(allNamesMasc) - 1 < 0 or len(allNamesFem) - 1 < 0):
        print("Erro: Lista de nomes insuficiente")
        return
    if(genFem == False):
        personagem = allNamesMasc[FirstNameMasc] + " " + allNamesSbr[LastName]
        allNamesMasc.remove(allNamesMasc[FirstNameMasc])
        allNamesSbr.remove(allNamesSbr[LastName])
    else:
        personagem = allNamesFem[FirstNameFem] + " " + allNamesSbr[LastName]
        allNamesFem.remove(allNamesFem[FirstNameFem])
        allNamesSbr.remove(allNamesSbr[LastName])
    return personagem

""" print(CharacterGenerator(genFem= False))
print(CharacterGenerator(genFem= True)) """
if (openTest):
    listNamesMasc.close()
    listNamesFem.close()
    listNamesSbr.close()