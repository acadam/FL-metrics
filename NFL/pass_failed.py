

class PassFailed():
    def __init__(self, pass_fail_file):
        self.pass_failed_dict = self.read_pass_failed_data(pass_fail_file)
        self.number_of_failed = 0
        self.number_of_pass = 0


    def read_pass_failed_data(self, pass_fail_file):
        F = open(pass_fail_file, "r")
        lines = F.readlines() # beolvassa az osszes sort
        tesztek=list(lines[0].split("\n")[0].split(";")[1:-2])

        pass_failed_dict={}
        for x in tesztek:
            pass_failed_dict[x]=str(1)

        eredmeny=list(lines[1].split("\n")[0].split(";")[1:-2])

        for x in range(0, len(eredmeny)):
            if int(eredmeny[x])==0:
                pass_failed_dict[ tesztek[x]]=str(0)
        F.close()

        return pass_failed_dict


    def set_number_of_tests(self):
        self.calc_number_of_failed()
        self.calc_number_of_pass()


    def calc_number_of_failed(self):
        for teszt, eredmeny in self.pass_failed_dict.items():
            if str(eredmeny) == str(0):
                self.number_of_failed += 1


    def calc_number_of_pass(self):
        for teszt, eredmeny in self.pass_failed_dict.items():
            if str(eredmeny) == str(1):
                self.number_of_pass += 1


    def fedett_tesztek_kozott_failed(self, fedett_tesztek):
        failed = 0
        for teszt in fedett_tesztek:
            if self.pass_failed_dict[teszt] == str(0):
                failed += 1
        return failed


    def fedett_tesztek_kozott_pass(self, fedett_tesztek):
        pass_teszt = 0
        for teszt in fedett_tesztek:
            if self.pass_failed_dict[teszt] == str(1):
                pass_teszt += 1
        return pass_teszt


    def get_buko_tesztek(self):
        buko_tesztek = set()
        for teszt, eredmeny in self.pass_failed_dict.items():
            if eredmeny == str(0):
                buko_tesztek.add(teszt)
        return buko_tesztek
