# fill_tax.py

A Python program to fill taxonomy assessed by sintax presenting one or more missing ranks.  
Missing ranks are filled with the last rank provided with suffix "_Species" for Species rank, _Genus for genus rank and so on... 

example usage: ./fill_tax.py -i seed_sintax.csv -o out_filled_tax.txt

# fill_tax_biom.py
To fill incomplete taxonomy from TSV formatted biom files.
./fill_tax_biom.py -i biom-feature-table-w-taxo.tsv -o out_filled_tax.txt
