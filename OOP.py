#összetartozóadatokat együtt akarunk kezelni: OOP- objektumorientált programozás 
#class:sablon, tudjuk, hogy milyen tulajdonságokkal, metódusollal rendelkezik az osztály. Az obejektum konkrét erékkel feltöltött példány
# class elnvezés nem mindig NAGYBETŰ

class Szemely:
    #tulajdonságok: adattag, foeld, osztályváltozó
    #név, életkor, magasság, táplálkozás, tömeg, fürdés
    #képességek: metódusok
    #táplálkozás, fürdés
    nev=""
    eletkor = 0
    magassag = 0 
    tomeg = 0
    def __init__(self, nevecske,eletkor, magassag , tomeg):
        self.nev = nevecske
        self.eletkor = eletkor
        self.magassag = magassag
        self.tomeg = tomeg

    def __str__(self):
        return f"{self.nev} {self.eletkor}"
        
        


    def taplalkozas(self, mennyiseg):
        self.tomeg += mennyiseg
    def sportolas(self, mennyiseg):
        if self.tomeg - mennyiseg > 1:
            self.tomeg -= mennyiseg

def peldanyostas(): 
    joska = Szemely()
    print(joska.nev)
    print(joska.eletkor)
    print(joska.magassag)

def pedanyositasInitenKeresztul():
    joska = Szemely("joska", 58, 175, 75.2)
    print(joska)
    print(joska.nev)
    print(joska.eletkor)
    bozsi = Szemely("Bözsi", 79, 200, 102)
    print(bozsi)
    print(bozsi.nev)
    print(bozsi.eletkor)
szemelyek = []
def falu():
    szemelyek.append(Szemely("joska", 58, 175, 75.2))
    szemelyek.append(Szemely("Bözsi", 79, 200, 102))
    szemelyek.append(Szemely("Géza", 35, 160, 52.2))
    szemelyek.append(Szemely("Böszike", 34, 155, 45.2))
    print(*szemelyek, sep= "\n")
    print("-----------------------------------------")
    for item in szemelyek:
        print(f"{item.nev} {item.eletkor}")


def main():
   #pedanyositasInitenKeresztul()
    falu()
main()


