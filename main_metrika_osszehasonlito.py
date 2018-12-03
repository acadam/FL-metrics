import sys

"""
input csv:
GP1;GP2;...;NFL-1;NFL-2;NFL-3;NFL-4
1.5;1.5;1.5;1.5;1.5;1.5;124.5;1.5;1.5;1.5;1.5;25.5;1.5;1.5;1.5;1.5
"""

def csv_beolvasas():
    compare_dict = {}
    metrikak = list()
    with open(sys.argv[1]) as csv_file:
        lines = csv_file.readlines()
        metrikak = list(lines[0].split("\n")[0].split(";")[:])

        for metrika1 in metrikak:
            compare_dict[metrika1] = {}
            for metrika2 in metrikak:
                if metrika1 != metrika2:
                    compare_dict[metrika1][metrika2] = {}
                    compare_dict[metrika1][metrika2]["="] = 0
                    compare_dict[metrika1][metrika2]["<"] = 0
                    compare_dict[metrika1][metrika2][">"] = 0

        for x in range(1, len(lines)):
            ranks = list(lines[x].split("\n")[0].split(";")[:])

            for _m1 in range(len(metrikak)):
                for _m2 in range(len(metrikak)):
                    if _m1 != _m2:
                        if float(ranks[_m1]) > float(ranks[_m2]):
                            compare_dict[metrikak[_m1]][metrikak[_m2]][">"] += 1
                        elif float(ranks[_m1]) == float(ranks[_m2]):
                            compare_dict[metrikak[_m1]][metrikak[_m2]]["="] += 1
                        elif float(ranks[_m1]) < float(ranks[_m2]):
                            compare_dict[metrikak[_m1]][metrikak[_m2]]["<"] += 1
    return compare_dict, metrikak


def kisebb_dump(metrikak, compare_dict):
    fejlec = "<"
    for m in metrikak:
        fejlec += ";"+str(m)
    print(fejlec)

    for m1 in metrikak:
        osszehas = str(m1)
        for m2 in metrikak:
            if m1 == m2:
                osszehas += ";X"
            else:
                osszehas += ";"+str(compare_dict[m1][m2]["<"])
        print(osszehas)



def egyenlo_dump(metrikak, compare_dict):
    fejlec = "="
    for m in metrikak:
        fejlec += ";"+str(m)
    print(fejlec)

    for m1 in metrikak:
        osszehas = str(m1)
        for m2 in metrikak:
            if m1 == m2:
                osszehas += ";X"
            else:
                osszehas += ";"+str(compare_dict[m1][m2]["="])
        print(osszehas)


compare_dict, metrikak = csv_beolvasas()
kisebb_dump(metrikak, compare_dict)
print("\n\n")
egyenlo_dump(metrikak, compare_dict)

