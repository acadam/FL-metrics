import scipy.stats as ss


def rank_calculate(hibas_metodus_tippek):
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

    #print(infection_ranks)
    return infection_ranks

