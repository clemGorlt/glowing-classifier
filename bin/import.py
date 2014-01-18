import argparse
import sys
import redis
import hashlib

r=redis.StrictRedis(host='localhost', port=6379, db=0)
argParser = argparse.ArgumentParser(description='Pcap Classifier')
argParser.add_argument('-f',action='append', help='Filename')
args = argParser.parse_args()

if args.f is not None:
	#filename = args.f
	filename=args.f[0].split(".")[0]#ce qu'il y a devant le .
	r.sadd("processed",filename)
	print("filename: "+filename)
	
	md5 = filename
	lnumber=0
	field=None
	for line in sys.stdin:
		if lnumber == 0: #entete car tshark a -E header=yes
			fields=line.rstrip().split(",")
			for field in fields:
				r.sadd("type",field)
		else:
			elements=line.rstrip().split(",")
			i=0
			for element in elements:
				try:
					r.sadd("0:"+fields[i],element)
					ehash=hashlib.md5()
					ehash.update(element.encode("utf-8"))
					ehhex=ehash.hexdigest()
					if element is not "":
						r.sadd("v:"+ehhex,md5)
				except IndexError:
					print("Empty Field!!")
				i=i+1
		lnumber=lnumber+1
else:
	argParser.print_help()

