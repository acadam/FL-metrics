import subprocess as sp
import id_parser
import os

for x in range(1, 28):
    if x == 1:
        if os.path.exists("results-joda-time.csv"):
            os.remove("results-joda-time.csv")
            print("result-joda-time.csv successfully deleted.")
        if os.path.exists("all-results.csv"):
            os.remove("all-results.csv")
            print("all-results.csv successfully deleted.")

    cmd_str = "../../build/cl/SoDATools/fl-score/fl-score"
    cmd_str2= "../../build/cl/SoDATools/utilities/binarydump/binaryDump"
    cmd_str = cmd_str+" --coverage-matrix ../../bugs/joda-time/joda-time."+str(x)+"b.method.cov.SoDA"
    cmd_str = cmd_str+" --results-matrix ../../bugs/joda-time/joda-time."+str(x)+"b.res.SoDA"
    cmd_str = cmd_str+" --changeset ../../bugs/joda-time.chg.SoDA"
    cmd_str = cmd_str+" --output-dir ."
    cmd_str2 = cmd_str2+" -c ../../bugs/joda-time/joda-time."+str(x)+"b.method.cov.SoDA"
    cmd_str2 = cmd_str2+" --dump-coverage-code-elements "+str(x)
    sp.call(cmd_str, shell=True)
    sp.call(cmd_str2, shell=True)
    id_parser.id_parse(x, "joda-time")

for x in range(1, 54):
    if x == 1:
        if os.path.exists("results-commons-lang.csv"):
            os.remove("results-commons-lang.csv")
            print("result-commons-lang.csv successfully deleted.")
            
    if os.path.exists("../../bugs/commons-lang/commons-lang."+str(x)+"b.method.cov.SoDA") == False:
        continue

    cmd_str = "../../build/cl/SoDATools/fl-score/fl-score"
    cmd_str2= "../../build/cl/SoDATools/utilities/binarydump/binaryDump"
    cmd_str = cmd_str+" --coverage-matrix ../../bugs/commons-lang/commons-lang."+str(x)+"b.method.cov.SoDA"
    cmd_str = cmd_str+" --results-matrix ../../bugs/commons-lang/commons-lang."+str(x)+"b.res.SoDA"
    cmd_str = cmd_str+" --changeset ../../bugs/joda-time.chg.SoDA"
    cmd_str = cmd_str+" --output-dir ."
    cmd_str2 = cmd_str2+" -c ../../bugs/commons-lang/commons-lang."+str(x)+"b.method.cov.SoDA"
    cmd_str2 = cmd_str2+" --dump-coverage-code-elements "+str(x)
    sp.call(cmd_str, shell=True)
    sp.call(cmd_str2, shell=True)
    id_parser.id_parse(x, "commons-lang")

for x in range(1, 105):
    if x == 1:
        if os.path.exists("results-commons-math.csv"):
            os.remove("results-commons-math.csv")
            print("result-commons-math.csv successfully deleted.")

    if os.path.exists("../../bugs/commons-math/commons-math."+str(x)+"b.method.cov.SoDA") == False:
        continue

    cmd_str = "../../build/cl/SoDATools/fl-score/fl-score"
    cmd_str2= "../../build/cl/SoDATools/utilities/binarydump/binaryDump"
    cmd_str = cmd_str+" --coverage-matrix ../../bugs/commons-math/commons-math."+str(x)+"b.method.cov.SoDA"
    cmd_str = cmd_str+" --results-matrix ../../bugs/commons-math/commons-math."+str(x)+"b.res.SoDA"
    cmd_str = cmd_str+" --changeset ../../bugs/joda-time.chg.SoDA"
    cmd_str = cmd_str+" --output-dir ."
    cmd_str2 = cmd_str2+" -c ../../bugs/commons-math/commons-math."+str(x)+"b.method.cov.SoDA"
    cmd_str2 = cmd_str2+" --dump-coverage-code-elements "+str(x)
    sp.call(cmd_str, shell=True)
    sp.call(cmd_str2, shell=True)
    id_parser.id_parse(x, "commons-math")

for x in range(1, 27):
    if x == 1:
        if os.path.exists("results-jfreechart.csv"):
            os.remove("results-jfreechart.csv")
            print("result-jfreechart.csv successfully deleted.")

    if os.path.exists("../../bugs/jfreechart/jfreechart."+str(x)+"b.method.cov.SoDA") == False:
        continue

    cmd_str = "../../build/cl/SoDATools/fl-score/fl-score"
    cmd_str2= "../../build/cl/SoDATools/utilities/binarydump/binaryDump"
    cmd_str = cmd_str+" --coverage-matrix ../../bugs/jfreechart/jfreechart."+str(x)+"b.method.cov.SoDA"
    cmd_str = cmd_str+" --results-matrix ../../bugs/jfreechart/jfreechart."+str(x)+"b.res.SoDA"
    cmd_str = cmd_str+" --changeset ../../bugs/joda-time.chg.SoDA"
    cmd_str = cmd_str+" --output-dir ."
    cmd_str2 = cmd_str2+" -c ../../bugs/jfreechart/jfreechart."+str(x)+"b.method.cov.SoDA"
    cmd_str2 = cmd_str2+" --dump-coverage-code-elements "+str(x)
    sp.call(cmd_str, shell=True)
    sp.call(cmd_str2, shell=True)
    id_parser.id_parse(x, "jfreechart")
