voiture = {
    'date_construction': "2018-12-20",
    'couleur': "rouge",
    'proprietaire': "titouan",
    'numero': "XX-999-XX"
    }

class Voiture(object):
    def __init__(self, date_construction, couleur, proprietaire, numero):
        self.date_construction = date_construction
        self.couleur = couleur
        self.proprietaire = proprietaire
        self.numero = numero

    def __str__(self, *args, **kwargs):
        return "Voiture(numero={numero})".format(**self.__dict__)

def main():
    """ fonction du programme principal
    """
    print(voiture)
    print("Voiture(numero={numero})".format(**voiture))

    search_is = "XX-999-XX"
    for clef, valeur in voiture.items():
        if valeur == search_is:
            print(clef)

    voiture1 = Voiture("1970-01-01", "bleu", "toto", "123-ABC-456")
    print(voiture1)

if __name__ == "__main__":
    main()
