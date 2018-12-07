import arg_parser
import bugs
import scores
import coverage
import pass_failed
import ranks


param_dict = arg_parser.arg_parser()
#print("*** "+str(param_dict["bugID"])+" ***")


cov = coverage.Coverage(param_dict["coverage"], param_dict["map"])
cov.graf_kinyerese(param_dict["coverage"])



bug = bugs.BugInfo(param_dict["results"], param_dict["change"], param_dict["bugID"])



teszteredmenyek = pass_failed.PassFailed(param_dict["results"])
teszteredmenyek.set_number_of_tests()



metodusok = scores.Metodusok( cov.metodusnevek )
metodusok.score_szamitas(teszteredmenyek, cov.graf)



sum_rank = ranks.Ranks(cov.metodusnevek)
sum_rank.all_rank_calc(metodusok.metrika_lista)

sum_rank.print_min_ranks(bug.hiba_helyei)
