import NFL_metrics


class Metodusok():
    def __init__(self, metodusnevek):
        self.metodusnevek_lista = list(metodusnevek)
        self.metrika_lista = {}

        buko_tesztek = teszteredmenyek.get_buko_tesztek()

        NFL = NFL_metrics.NFL_Metric(self.metodusnevek_lista)
        NFL.neighborsFL(graf, self.metodusnevek_lista, buko_tesztek)

        self.metrika_lista["NFL"] = NFL

