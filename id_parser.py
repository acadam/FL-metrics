import json
import csv
import rank
from pathlib import Path


def id_parse(x, bug_class):
    with open('result-0.json', 'r') as json_data:
        results = json.load(json_data)

    json_data.close()

    csv_rows = {}
    with open(str(x)+'.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=':')
        for row in csv_reader:
            csv_rows[row[0]] = row[1]

    csv_file.close()

    names = {}
    tracesNames = open("../../bugs/"+str(bug_class)+"/"+str(bug_class)+"."+str(x)+"b.traces.names.txt", "r")
    for name in tracesNames:
        a = name.split(':')[1]
        b = name.split(':')[0]
        names[a] = b

    for method_name, method_id in names.items():
        for id1, id2 in csv_rows.items():
            if method_id == id2:
                names[method_name] = id1

    dict_for_ranking = {}
    for method_name, method_id in names.items():
        for m_id, name in results["full"].items():
            if method_id == m_id:
                dict_for_ranking[method_name] = results["full"][str(m_id)]

    barinel = {}
    drt = {}
    dstar = {}
    jaccard = {}
    kulczynski2 = {}
    mccon = {}
    minus = {}
    ochiai = {}
    op2 = {}
    tarantula = {}
    wong3 = {}
    zoltar = {}

    for method_name, name in dict_for_ranking.items():
        for fl_metric, score in name.items():
            if str(fl_metric) == "barinel":
                barinel[method_name] = score
            if str(fl_metric) == "drt":
                drt[method_name] = score
            if str(fl_metric) == "dstar":
                dstar[method_name] = score
            if str(fl_metric) == "jaccard":
                jaccard[method_name] = score
            if str(fl_metric) == "kulczynksi2":
                kulczynski2[method_name] = score
            if str(fl_metric) == "mccon":
                mccon[method_name] = score
            if str(fl_metric) == "minus":
                minus[method_name] = score
            if str(fl_metric) == "ochiai":
                ochiai[method_name] = score
            if str(fl_metric) == "Op2":
                op2[method_name] = score
            if str(fl_metric) == "tarantula":
                tarantula[method_name] = score
            if str(fl_metric) == "wong3":
                wong3[method_name] = score
            if str(fl_metric) == "zoltar":
                zoltar[method_name] = score


    barinel = rank.rank_calculate(barinel)
    drt = rank.rank_calculate(drt)
    dstar = rank.rank_calculate(dstar)
    jaccard = rank.rank_calculate(jaccard)
    kulczynski2 = rank.rank_calculate(kulczynski2)
    mccon = rank.rank_calculate(mccon)
    minus = rank.rank_calculate(minus)
    ochiai = rank.rank_calculate(ochiai)
    op2 = rank.rank_calculate(op2)
    tarantula = rank.rank_calculate(tarantula)
    wong3 = rank.rank_calculate(wong3)
    zoltar = rank.rank_calculate(zoltar)

    for method_name, name in dict_for_ranking.items():
        for method_name2, ranks in barinel.items():
            if method_name == method_name2:
                dict_for_ranking[method_name]["barinel"] = ranks
        for method_name2, ranks in drt.items():
            if method_name == method_name2:
                dict_for_ranking[method_name]["drt"] = ranks
        for method_name2, ranks in dstar.items():
            if method_name == method_name2:
                dict_for_ranking[method_name]["dstar"] = ranks
        for method_name2, ranks in jaccard.items():
            if method_name == method_name2:
                dict_for_ranking[method_name]["jaccard"] = ranks
        for method_name2, ranks in kulczynski2.items():
            if method_name == method_name2:
                dict_for_ranking[method_name]["kulczynksi2"] = ranks
        for method_name2, ranks in mccon.items():
            if method_name == method_name2:
                dict_for_ranking[method_name]["mccon"] = ranks
        for method_name2, ranks in minus.items():
            if method_name == method_name2:
                dict_for_ranking[method_name]["minus"] = ranks
        for method_name2, ranks in ochiai.items():
            if method_name == method_name2:
                dict_for_ranking[method_name]["ochiai"] = ranks
        for method_name2, ranks in op2.items():
            if method_name == method_name2:
                dict_for_ranking[method_name]["Op2"] = ranks
        for method_name2, ranks in tarantula.items():
            if method_name == method_name2:
                dict_for_ranking[method_name]["tarantula"] = ranks
        for method_name2, ranks in wong3.items():
            if method_name == method_name2:
                dict_for_ranking[method_name]["wong3"] = ranks
        for method_name2, ranks in zoltar.items():
            if method_name == method_name2:
                dict_for_ranking[method_name]["zoltar"] = ranks

    changed_methods = {}
    with open('../../bugs/'+str(bug_class)+'/'+str(bug_class)+'-changes.csv', mode='r') as csv_changed:
        if str(bug_class) == "joda-time" or str(bug_class) == "commons-lang":
            csv_reader = csv.reader(csv_changed, delimiter=";")
            for row in csv_reader:
                if row[1] == str(x):
                    for method_name, ranks in dict_for_ranking.items():
                        a = str(method_name).split('\n')[0]
                        if a == row[2]:
                            changed_methods[row[2]] = ranks
        else:
            csv_reader = csv.reader(csv_changed, delimiter=";")
            for row in csv_reader:
                if row[1] == str(x):
                    full_method_name_list = []
                    if len(row) < 4:
                        full_method_name_string = str(row[2])
                    else:
                        for y in range(2, len(row)):
                            full_method_name_list.append(row[y])
                        full_method_name_string = ";".join(full_method_name_list)
                    for method_name, ranks in dict_for_ranking.items():
                        a = str(method_name).split('\n')[0]
                        if str(a) == str(full_method_name_string):
                            changed_methods[full_method_name_string] = ranks

    csv_changed.close()

    final_result = {}
    if len(changed_methods) == 1:
        for method_name, ranks in changed_methods.items():
            final_result = changed_methods[method_name]
    else:
        counter = 1
        for method_name, ranks in changed_methods.items():
            if counter == 1:
                final_result = ranks
            for method_name2, ranks2 in changed_methods.items():
                if already_exists(method_name, final_result) == True:
                    continue
                if method_name != method_name2:
                    for fl_name, exact_rank in ranks.items():
                        for fl_name2, exact_rank2 in ranks2.items():
                            if fl_name == fl_name2:
                                a = changed_methods[str(method_name)][str(fl_name)]
                                b = changed_methods[str(method_name2)][str(fl_name)]
                                c = final_result[fl_name]
                                if a <= b:
                                    if a <= c:
                                        final_result[fl_name] = exact_rank
                                elif b <= c:
                                    final_result[fl_name] = exact_rank2
                                else:
                                    counter += 1
                                    continue
            counter += 1
    print("VERZIO "+str(x))
    print(final_result)

    fl_name_list= ["barinel", "drt", "dstar", "jaccard", "kulczynksi2", "mccon", "minus", "ochiai", "Op2", "tarantula", "wong3", "zoltar"]

    result_csv = Path("results-"+str(bug_class)+".csv")
    csv.register_dialect('myDialect', delimiter = ';')
    if result_csv.is_file():
        with open('results-'+str(bug_class)+'.csv', 'a') as csvfile:
            writer = csv.writer(csvfile, dialect='myDialect')
            final_score_list = final_score(fl_name_list, final_result)
            writer.writerow(final_score_list)
    else:
        with open('results-'+str(bug_class)+'.csv', 'w') as csvfile:
            writer = csv.writer(csvfile, dialect='myDialect')
            writer.writerow(fl_name_list)
            final_score_list = final_score(fl_name_list, final_result)
            writer.writerow(final_score_list)

    all_results_csv = Path("all-results.csv")
    csv.register_dialect('myDialect', delimiter = ';')
    if all_results_csv.is_file():
        with open('all-results.csv', 'a') as csvfile:
            writer = csv.writer(csvfile, dialect='myDialect')
            final_score_list = final_score(fl_name_list, final_result)
            writer.writerow(final_score_list)
    else:
        with open('all-results.csv', 'w') as csvfile:
            writer = csv.writer(csvfile, dialect='myDialect')
            writer.writerow(fl_name_list)
            final_score_list = final_score(fl_name_list, final_result)
            writer.writerow(final_score_list)




def already_exists(method, final_result):
    for method_name, name in final_result.items():
        if method == method_name:
            return True
        else:
            return False

def final_score(fl_name_list, final_result):
    final_score_list = []
    for x in fl_name_list:
        for fl_name, score in final_result.items():
            if x == str(fl_name):
                final_score_list.append(score)

    return final_score_list

