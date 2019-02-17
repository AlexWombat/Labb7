class DictHash:

    def __init__(self):
        self.dictionary = {}

    def store(self, nyckel, värde):
        self.dictionary[nyckel] = värde

    def __getitem__(self, nyckel):
        return self.dictionary[nyckel]

    def __contains__(self, nyckel):
        if nyckel in self.dictionary:
            return True


if __name__ == '__main__':
    htabell = DictHash()
    htabell.store('Abba', 'Mamma Mia')
    print(htabell['Abba'])