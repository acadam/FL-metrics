import scipy.stats as ss


class Ranks():
    def __init__(self, metodusnevek):
        self.nfl = self.init_metodus_ranks_dict(metodusnevek)

    def init_metodus_ranks_dict(self, metodusnevek):
        _metodus_rank_dict = {}
        for m in metodusnevek:
            _metodus_rank_dict[m] = 0
        return _metodus_rank_dict



    def all_rank_calc(self, metodusok_metrikaLista):
        self.nfl = self._rank_calc(metodusok_metrikaLista["NFL"].score)

    def _rank_calc(self, metodus_score_dict):
        elem_vektor=[]
        tippeles_vektor=[]
        eredmeny = sorted(metodus_score_dict, key=metodus_score_dict.__getitem__, reverse=True)
        for elem in eredmeny:
            elem_vektor.append(elem)
            tippeles_vektor.append( abs(max(metodus_score_dict.values()) - metodus_score_dict[elem]))
        rank_vektor = ss.rankdata(tippeles_vektor,method='average')


        infection_ranks = {}
        for x in range(len(elem_vektor)):
            infection_ranks[elem_vektor[x]] = rank_vektor[x]

        return infection_ranks


    def print_min_ranks(self, hiba_helyei):
        print(str(min(self.get_hibahely_rank_list(hiba_helyei, self.nfl)))+";")


    def get_hibahely_rank_list(self, hiba_helyei, ranks):
        hiba_ranks = list()
        for hiba in hiba_helyei:
            hiba_ranks.append( ranks[hiba] )
        return hiba_ranks
