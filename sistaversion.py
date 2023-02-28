#Laboration 7
#Tillämpad datalogi Erik Hellström, Eyasu Alemiye
#Andra halvan av laboration 7


#använder den nod som givits oss i uppgiftsbeskrivningen
class HashNode:
    def __init__(self, key, data = None, next = None):
        self.key = key
        self.data = data
        self.next = next



#Använder en magic method för att skapa en sträng-representation av Nodobjektet
    def __str__(self):
        return self.key + " finns och har följande egenskaper: "+ self.data
    
#klass för att skapa Hashtabellen
class Hashtable:
    #Använder init-konstruktor från kap 6.5 med skillnaden att hashtabellens storlek tas som inparameter och att ett attribut är antalet krockar.
    def __init__(self, size):
        self.size = size
        self.slot = [None] * self.size
        self.data = [None] * self.size
        self.krockar = 0

    def getKey(self):
        return self.key

    def getNext(self):
        return self.next




    #hashfunktion från boken kap 6.5. Tar namn = key som inparameter och omvandlar till en sifferkombination
    def hashfunction(self, key):
        sum = 0
        for pos in range(len(key)):
            sum = sum + ord(key[pos])
        #print(sum%self.size) #Använder denna för att se vilka index som skapas
        return sum%self.size
    


    
    def store(self, key, data):
        #skapar ett index för key. dvs gör om namnet till en sifferkombination genom att kalla på hashfunktionsmetoden
        slot_nummer = self.hashfunction(key)
        #print("det framtagna hashvärdet är "+ str(slot_nummer) +" till namnet " + key) #DENNA ANVÄNDS FÖR ATT KONTROLLERA ATT POKEMONNAMN HAR FÅTT ETT KORREKT HASHVÄRDE


        #Om det inte uppstår någon krock dvs om sloten = None
        #If-satsen liknar kod-segmentet från listing 3 i kap 6.5
        if self.slot[slot_nummer] == None:
            #Om slot = None för den aktuella platsen sätts noden in på den platsen
            self.slot[slot_nummer] = HashNode(key, data)
            
        #om det uppstår en krock exekveras nedan --> använder open addressing i form av linear probing
        else:
            krock = self.slot[slot_nummer]
            self.slot[slot_nummer] = HashNode(key, data)
            self.slot[slot_nummer].next = krock
            self.krockar += 1
        return self.krockar



    def search(self,sökord):
        slot_nummer = self.hashfunction(sökord)
        noden = self.slot[slot_nummer]
        

        if noden == None:
            #print("A")
            raise KeyError
        
        if noden.key == sökord:
            #print("B")
            return noden
            
        if noden != None:
            while noden != None:
                if noden.key == sökord:
                    #print("C")
                    return noden
                
                if noden == None:
                    #print("D")
                    raise KeyError
                    
                else: 
                    #print("E")
                    noden = noden.next

            raise KeyError
                    


#hämtar input från användaren för att kunna söka efter olika pokemons i koden
def input_användare():
    sökning = input("Hej, vad önskar du söka efter: ")
    return sökning

#läsen in 
def läs_in():
    with open(r"pokemon.csv", "r", encoding = "utf-8") as allapokemons:
            for rad in allapokemons:
                pokemon= rad.strip()
                specifikinfo=pokemon.split(',')  
                key=specifikinfo[1]
                data = "\nType 1: "+specifikinfo[2] +"\nType 2: "+ specifikinfo[3] +"\nTotal: "+ specifikinfo[4] +"\nHP: " + specifikinfo[5] +"\nAttack: "+ specifikinfo[6] +"\nDefense: "+ specifikinfo[7] +"\nSp. Atk: "+ specifikinfo[8] +"\nSp. Def: "+ specifikinfo[9] +"\nSpeed: "+ specifikinfo[10] +"\nGeneration: "+ specifikinfo[11] +"\nLegendary: "+ specifikinfo[12]
                krockar = tabell.store(key,data)
            return krockar




#______________ANROP___________________________ANROP___________________________ANROP___________________________ANROP_____________
storlek_hashtable = 4
tabell = Hashtable(storlek_hashtable)
print("\nI en hashtabell med " +str(storlek_hashtable) + "st slots uppstår "+ str(läs_in())+ "st krockar.")
sökning = input_användare()

print(tabell.search(sökning))
