#!/usr/bin/env python3
#Fill incomplete tax from TSV formatted biom files.
#./fill_tax_biom.py -i biom-feature-table-w-taxo.tsv -o out_filled_tax.txt

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

		if '#' in li:
			print("\t".join(lik))
		else:
			IndexTax=len(lik)-1
			tax=lik[IndexTax]
			Otu=lik[0]
			
			tax_s=tax.split(sep=';')


			FILL=[None] * 7
			for i in range(0,7):
				if(len(tax_s[i])>3):
					LAST=tax_s[i]
					FILL[i]=tax_s[i]
				else:
					FILL[i]=tax_s[i]+LAST[3:]
			finalTax=";".join(FILL)

			lik[IndexTax]=finalTax
			print("\t".join(lik))

def _set_options ():
	parser = argparse.ArgumentParser()
	parser.add_argument('-i','--i-biom-tsvtable',action='store',required=True,type=str,dest='input',help='TSV formatted biom file with taxonomy.')
	parser.add_argument('-o','--output_name',action='store',default='out_filltax.txt',type=str,dest='outname',help='Output filename.')
	args = parser.parse_args()
	return args


if __name__ == "__main__":
	main()