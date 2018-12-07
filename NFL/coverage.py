import networkx as nx


class Coverage():
    def __init__(self, input_matrix, nevmap_file):
        self.graf = nx.Graph()
        self.tesztnevek = self._tesztnevek_kinyerese(input_matrix)
        self.metodusnevek = self._metodusnevek_kinyerese(input_matrix, nevmap_file)


    def _metodusnevek_kinyerese(self, input_matrix, nevmap_file):
        nevmap = self._nevmapper_beolvasasa(nevmap_file)
        matrix = open(input_matrix)
        lines = matrix.readlines()
        metodus_lista = list()
        for x in list(lines[0].split("\n")[0].split(";")[1:]):
            if nevmap_file != None:
                metodus_lista.append(nevmap[x])
            else:
                metodus_lista.append(x)
        matrix.close()
        return metodus_lista


    def _nevmapper_beolvasasa(self, nevmap_file):
        name_map={}
        with open(nevmap_file, 'r') as infile:
            for line in infile:
                ID = line.split(":")[0]
                name=line.split(":")[1].split("\n")[0]
                name_map[ID]=name
        return name_map


    def _tesztnevek_kinyerese(self, input_matrix):
        matrix = open(input_matrix)
        teszt_lista = list()
        lines = matrix.readlines()
        for x in range(len(lines)):
            if len(lines[x].split(";")[0]) > 0:
                teszt_lista.append( lines[x].split(";")[0] )
        matrix.close()
        return teszt_lista

    def graf_kinyerese(self, input_matrix):

        self._csucsok_hozzaadasa()

        matrix = open(input_matrix)
        lines = matrix.readlines()
        for x in range(1,len(lines)):
            line = lines[x].split("\n")[0]
            ertek_lista = list(line.split(";")[1:])
            for y in range(len(ertek_lista)):
                if int(ertek_lista[y]) == 1:
                    self.graf.add_edge(self.tesztnevek[x-1], self.metodusnevek[y])
        matrix.close()


    def _csucsok_hozzaadasa(self):
        for teszt in self.tesztnevek:
            self.graf.add_node(teszt, label=teszt)

        for metodus in self.metodusnevek:
            self.graf.add_node(metodus, label=metodus)

