#!/usr/bin/env python3
#Fill incomplete tax from sintax files.
#./fill_tax.py -i seed_sintax2.csv -o out_filled_tax.txt

import argparse, sys, getopt


def main ():
	options = _set_options()
	sys.stdout = open(options.outname,'wt')
	_fill_tax(options)

def _fill_tax (options):
	filin = open(options.input,"r")
	for li in filin:
		lip=li.rstrip("\n")
		lik=lip.split(sep='\t')
		tax=lik[3]
		Otu=lik[0].split(sep=' ')[0]
		tax_s=tax.split(sep=',')
		RANK=len(tax_s)
		if RANK==7:
			print(Otu,"\t",tax, sep="")
		elif RANK==6:
			lastRank=tax_s[RANK-1].split(sep=":")[1]
			print(Otu,"\t",tax,",s:",lastRank,"_Species" , sep="")
		elif RANK==5:
			lastRank=tax_s[RANK-1].split(sep=":")[1]
			print(Otu,"\t",tax,",g:",lastRank,"_Genus" ,",s:",lastRank,"_Species" , sep="")
		elif RANK==4:
			lastRank=tax_s[RANK-1].split(sep=":")[1]
			print(Otu,"\t",tax,",f:",lastRank,"_Family" ,",g:",lastRank,"_Genus" ,",s:",lastRank,"_Species" , sep="")
		elif RANK==3:
			lastRank=tax_s[RANK-1].split(sep=":")[1]
			print(Otu,"\t",tax,",o:",lastRank,"_Order" ,",f:",lastRank,"_Family" ,",g:",lastRank,"_Genus" ,",s:",lastRank,"_Species" , sep="")
		elif RANK==2:
			lastRank=tax_s[RANK-1].split(sep=":")[1]
			print(Otu,"\t",tax,",c:",lastRank,"_Class" ,",o:",lastRank,"_Order" ,",f:",lastRank,"_Family" ,",g:",lastRank,"_Genus" ,",s:",lastRank,"_Species" , sep="")
		elif RANK==1:
			lastRank=tax_s[RANK-1].split(sep=":")[1]
			print(Otu,"\t",tax,",d:",lastRank,"_Domain" ,",c:",lastRank,"_Class" ,",o:",lastRank,"_Order" ,",f:",lastRank,"_Family" ,",g:",lastRank,"_Genus" ,",s:",lastRank,"_Species" , sep="")



def _set_options ():
	parser = argparse.ArgumentParser()
	parser.add_argument('-i','--i-sintax-taxtable',action='store',required=True,type=str,dest='input',help='Sintax file with taxonomy.')
	parser.add_argument('-o','--output_name',action='store',default='out_filltax.txt',type=str,dest='outname',help='Output filename.')
	args = parser.parse_args()
	return args


if __name__ == "__main__":
	main()