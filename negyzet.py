class NegyzetSikidom:
    hosszusag = 0 

    def __init__(self, hosszusag):
        self.hosszusag = hosszusag
    def Terulet(self):
        return self.hosszusag * self.hosszusag
    def kerulet(self):
        return self.hosszusag * 4

    def __str__(self):
        return f"hosszusag: {self.hosszusag}\nterület: {self.Terulet()}\nkerület: {self.kerulet()}"


negyzetek = []
def peldanyok():
    for i in range(1,6):
        negyzetek.append(NegyzetSikidom(i*10))
    for item in negyzetek:
        print(item)    
    
def peldanyok1():
    negyzetek.clear()
    for i in range(1,6):
        negyzetek.append(NegyzetSikidom(i*10))
    for item in negyzetek:
        print(item)
        



def main():
    peldanyok()
main()










