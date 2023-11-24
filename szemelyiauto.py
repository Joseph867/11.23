






class Szemelyiauto: 
    nev = " "
    loero = 0
    szin = " "
    evjarat = 0
    fogyasztas = 0 
    

    def __init__(self, nev, loero, szin,evjarat, fogyasztas):
        self.nev = nev
        self.loero = loero
        self.szin = szin 
        self.evjarat = evjarat
        self.fogyasztas = fogyasztas

    

def peldany():
    dodge = Szemelyiauto("Dodge challenger srt hellcat", 707, "bordó", 2015, 10)
    print(f"Neve: {dodge.nev}\nLóereje: {dodge.loero}\nSzíne: {dodge.szin}\nÉvjárat: {dodge.evjarat}\nMennyit fogyaszt: {dodge.fogyasztas} litert")

    


def main():
    peldany()
main()




