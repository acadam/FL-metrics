
class BugInfo():
    def __init__(self, pass_fail_file, change_file, bugID):
        self.buko_tesztek = self.hibas_test_calc(pass_fail_file)
        self.hiba_helyei = self.hiba_helye_calc(change_file, bugID)


    def hiba_helye_calc(self, change_file, bugID):
        _hiba_helye_set = set()
        with open(change_file, 'r') as infile:
            for line in infile:
                if line.startswith(";"+str(bugID)+";"):
                    _hiba_helye_set.add(";".join(line.split("\n")[0].split(";")[2:]))
        return _hiba_helye_set


    def hibas_test_calc(self, pass_fail_file):
        _buko_tesztek = set()
        F = open(pass_fail_file, "r")
        lines = F.readlines() # beolvassa az osszes sort
        tesztek=list(lines[0].split("\n")[0].split(";")[1:-2])
        eredmeny=list(lines[1].split("\n")[0].split(";")[1:-2])
        for x in range(0, len(eredmeny)):
            if str(eredmeny[x])==str(0):
                _buko_tesztek.add(tesztek[x])
        F.close()
        return _buko_tesztek
