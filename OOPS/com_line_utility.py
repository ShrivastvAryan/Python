import argparse

parser=argparse.ArgumentParser()

#Add command line arguments
parser.add_argument('url',help='url of the fiel to be downloaded')
parser.add_argument('arg2',help='description of arg2')

args=parser.parse_args() #parse the arguments

print(args.arg1)
print(args.arg2)