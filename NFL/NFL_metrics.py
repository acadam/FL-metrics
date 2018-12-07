import math
import scipy.stats as ss

class NFL_Metric:
    def __init__(self, metodusnev):
        self.score = self._score_init(metodusnev)


    def _score_init(self, metodusnev):
        _score = {}
        for metodus in metodusnev:
            _score[metodus] = 1.0
        return _score


    def alap_modell(self, graph, hibas_teszt, methods_names, ossz_hibas_el_count, szorzo=None):
        for node in graph.nodes():
            if node in hibas_teszt:
                if node in graph.nodes():
                    fedo_metodus = list(graph.neighbors(node))
                    jutalom = float(len(methods_names))/float(len(fedo_metodus))
                    for m in fedo_metodus:
                        self.score[m] += float(jutalom)/float(len(list(graph.neighbors(m))))

        for m in methods_names:
            if m in graph.nodes():
                metszet = set(list(graph.neighbors(m))).intersection(set(hibas_teszt))
                if szorzo==None:
                    self.score[m] = float(float(self.score[m])*float(len(metszet)))/float(ossz_hibas_el_count)
                else:
                    self.score[m] = float(float(self.score[m])*float(len(metszet)))/float(ossz_hibas_el_count)*szorzo[m]



    def rank_calculate(self, hibas_metodus_tippek):
        elem_vektor=[]
        tippeles_vektor=[]
        eredmeny = sorted(hibas_metodus_tippek, key=hibas_metodus_tippek.__getitem__, reverse=True)
        for elem in eredmeny:
            elem_vektor.append(elem)
            tippeles_vektor.append( abs(max(hibas_metodus_tippek.values()) - hibas_metodus_tippek[elem]))
        rank_vektor = ss.rankdata(tippeles_vektor,method='average')

        infection_ranks = {}
        for x in range(len(elem_vektor)):
            infection_ranks[elem_vektor[x]] = rank_vektor[x]

        return infection_ranks



    # *******************************************************************************


    def get_osszes_hibas_elszam(self, hibas_teszt, graph):
        ossz_hibas_el_count = 0
        for buko_teszt in hibas_teszt:
            if buko_teszt in graph.nodes():
                ossz_hibas_el_count += len(list(graph.neighbors(buko_teszt)))
        return ossz_hibas_el_count



    def nem_hibas_tesztek(self, graph, methods_names, hibas_teszt):
        teszt_set = set()
        for node in graph.nodes():
            if node not in methods_names and node not in hibas_teszt:
                teszt_set.add(node)
        return teszt_set



    def teszt_fedoMetodus_dict(self, graph, methods_names):
        test_neigh_dict={}
        for node in graph.nodes():
            if node not in methods_names:
                test_neigh_dict[node] = set(list(graph.neighbors(node)))
        return test_neigh_dict



    # *******************************************************************************


    def neighborsFL(self, graph, methods_names, hibas_teszt):
        ossz_hibas_el_count = self.get_osszes_hibas_elszam(hibas_teszt, graph)
        self.alap_modell(graph, hibas_teszt, methods_names, ossz_hibas_el_count)
