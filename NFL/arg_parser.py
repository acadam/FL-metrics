import argparse
import sys


def arg_parser():

    parser = argparse.ArgumentParser(description = 'ide jon valami')

    for i in range(len(sys.argv)):
        if sys.argv[i] == "-cF" or sys.argv[i] == "--configFile":
            parser.add_argument('-cF', '--configFile', help = 'config file')
            args_conf = parser.parse_args()
            return arg_from_file(args_conf.configFile)

    parser.add_argument('-c', '--coverage', required = True, help = 'coverage dump')
    parser.add_argument('-r', '--results', required = True, help = 'results dump')
    parser.add_argument('-x', '--change', required = True, help = 'changes file')
    parser.add_argument('-b', '--bugID', required = True, help = 'defects4j bugID')
    parser.add_argument('-o', '--output', required = True, help = 'output path')
    parser.add_argument('-m', '--map', help = 'methodID-name map csv')

    param_dict = {}
    args                = parser.parse_args()
    param_dict["coverage"] = args.coverage
    param_dict["results"] = args.results
    param_dict["change"] = args.change
    param_dict["bugID"] = args.bugID
    param_dict["output"] = args.output
    param_dict["map"] = args.map

    return param_dict


def arg_from_file(configFile):
    param_dict = {}
    with open(configFile, "r") as infile:
        for line in infile:
            arg = line.split("\n")[0].split("=")[0]
            val = line.split("\n")[0].split("=")[1]
            param_dict[arg] = val

    if "map" not in param_dict.keys():
        param_dict["map"] = None

    return param_dict