import argparse
from readFiles import read

parser = argparse.ArgumentParser()
parser.add_argument("-j", "--json", required=True)
args = vars(parser.parse_args())
read(args)







