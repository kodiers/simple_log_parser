# -*- coding: utf-8 -*-
import argparse

parser = argparse.ArgumentParser(description='Simple config parser')
parser.add_argument('-in', action='store', dest='in_file', help='File to parse')
parser.add_argument('-out', action='store', dest='out_file', help='Output file')
parser.add_argument('-search', action='store', dest='search', help='word to search')
parser.add_argument('-v', dest='verbose', help='verbose output', action='store_true')

args = parser.parse_args()

if not args.in_file or not args.out_file:
    print('In or Out file not set')
    exit()

if not args.search:
    print("Specify word to search")
    exit()

try:
    f = open(str(args.in_file), 'r')
except FileNotFoundError:
    print("In file doesn't exist")
    exit()

out = open(str(args.out_file), 'a')
lines = f.readlines()
i = 0
for line in lines:
    # For debug
    i += 1
    if args.verbose:
        print(i, line)
    try:
        if str(args.search).lower() in line.lower():
            out.write(line)
    except Exception:
        print('######### CANNOT READ STRING {} #########'.format(i))
        out.write('############# CANT READ STRING {}###########'.format(i))

f.close()
out.close()
