




class Kutya: 
    fajta = " "
    szin  = " "
    kor = 0 
    merete = " "
    suly = 0 

    def __init__(self, fajta, szin, neme, kor, merete, suly):
        self.fajta = fajta
        self.szin = szin 
        self.neme = neme
        self.kor = kor 
        self.merete = merete 
        self.suly = suly 


kutyusok = []
def peldany():
    kutyusok.append(Kutya("Németjuhász", "Fekete", "fiú", 9, 60, 32))
    kutyusok.append(Kutya("Dobermann", "Őzbarna", "lány", 5, 43, 24))
    kutyusok.append(Kutya("Dalmata", "Fekete-Fehér", "fiú", 6, 50, 26))
    kutyusok.append(Kutya("Vizsla", "Vörösbarna", "lány", 11, 57, 23))
    for dogs in kutyusok:
        print(f"Fajta: {dogs.fajta}, Színe: {dogs.szin}, Neme: {dogs.neme}, Életkora: {dogs.kor}, Mérete: {dogs.merete}, Súlya: {dogs.suly}")

def main():
    peldany()

main()

