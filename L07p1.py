from dicthash import DictHash


class Song:
    def __init__(self, artistid, artistnamn, sångtitel, låtlängd, år):
        self.artistid = artistid
        self.artistnamn = artistnamn
        self.sångtitel = sångtitel
        self.låtlängd = låtlängd
        self.år = år

    def __lt__(self, other):
        return float(self.låtlängd) < float(other.låtlängd)

    def __str__(self):
        return self.sångtitel + ' är skriven av ' + self.artistnamn + ' och är ' + self.låtlängd + 's lång.'


def readfile(filename):
    with open(filename, "r", encoding="utf-8") as låtfil:
        rader = låtfil.readlines()
        a = []
        for rad in rader:
            a.append(rad.strip('\n').strip().split('\t'))
        data = []
        for i in a:
            data.append(Song(i[0], i[1], i[2], i[3], i[4]))
        return data

def main():
    filename = 'sang-artist-data.txt'
    data = readfile(filename)
    hashtabell = DictHash()
    for i in data:
        hashtabell.store(i.sångtitel, i)
    söknyckel = 'Hallelujah'
    if söknyckel in hashtabell:
        print(hashtabell[söknyckel])         # detta kan jag göra eftersom jag har definierat metoden __getitem__
    else:
        print('Nyckeln finns inte.')


main()
