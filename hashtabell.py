class HashNode:
    def __init__(self, nyckel, värde):
        self.nyckel = nyckel
        self.värde = värde


class Hashtabell:
    def __init__(self, antalElement):
        self.storlek = round(antalElement*5)             # tumregel: minst 50% luft i tabellen
        self.tabell = [None]*self.storlek

    def put(self, nyckel, värde):
        nod = HashNode(nyckel, värde)
        index = self.hashfunction(nyckel)
        if self.tabell[index] is None:
            self.tabell[index] = nod
        elif self.tabell[index].nyckel == nyckel:
            self.tabell[index] = nod
        else:
            while self.tabell[index] is not None:        # linjär probning vid krock
                index = self.rehash(index)
            self.tabell[index] = nod
            return 1
        return 0

    def get(self, key):
        index = self.hashfunction(key)
        if self.tabell[index] is None:
            raise KeyError
        while self.tabell[index] is not None and self.tabell[index].nyckel != key:
            index = self.rehash(index)
            if self.tabell[index] is None:
                raise KeyError
        return self.tabell[index].värde

    def hashfunction(self, key):        # beräkna hashfunktionen för key
        tal = 0
        for i in key:                    # key[0] * 32**(n-1) + key[1]*32**(n-2) + ... + key[n-1]
            tal = tal*32 + ord(i)
        index = tal % self.storlek
        return index

    def rehash(self, key):                        # noden får ett nytt index
        return (key+1) % self.storlek


if __name__ == '__main__':
    htabell = Hashtabell(100)
    htabell.put('Abba', 'Mamma Mia')
    print(htabell.get('Abba'))
