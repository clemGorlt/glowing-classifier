import argparse
import sys
import redis

argParser = argparse.ArgumentParser(description='Pcap Classifier')
argParser.add_argument('-f',action='append', help='Filename')
args = argParser.parse_args()

if args.f is not None:
	filename = args.f
	for line in sys.stdin:
		a=line.split(",")
		print("src: "+a[0]+" SERVER: "+a[1])
else:
	argParser.print_help()
