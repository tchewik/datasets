import getopt
import sys
import pandas as pd
import re
import io
import string
from datetime import datetime
from tqdm import tqdm


def process(data, fileout):

    print('chunk processing started ...')
    timestart = datetime.now()
    children = data.loc[data['parent_id'] != 0] 

    # write pairs in <datasetname>.txt in acceptable format
    with io.open(fileout, 'a', encoding='utf8') as fo:
        for index, row in tqdm(children.iterrows()):
            parent_id = row.parent_id
            q = data.loc[data.id == parent_id, 'content']  # parent may not be in the chunk!
            if len(q):
                q = q.values[0]
                a = row.get('content')
                try:                  
                    fo.write(u'%s\n%s\n===\n' % (q, a))
                except TypeError:
                    pass

    timefinish = datetime.now()
    print('chunk processing succeed in {}'.format(timefinish - timestart) )


def main(argv):
    inputfile = None
    outputfile = None
    chunksize = 10 ** 9  # default value    

    try:
        opts, args = getopt.getopt(argv,"hi:o:s:",["ifile=","ofile=","chunksize="])
    except getopt.GetoptError:
        print('csv2txt.py -i <inputfile> -o <outputfile>')
        sys.exit(2) 
    for opt, arg in opts:
        if opt == '-h':
            print('csv2txt.py -i <inputfile> -o <outputfile> :: --chunksize <chunksize>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-s", "--chunksize"):
            chunksize = int(arg)

    if not inputfile or not outputfile:
        print('csv2txt.py -i <inputfile> -o <outputfile> :: --chunksize <chunksize>')
        sys.exit(2)


    print('csv2txt.py -i %s -o %s --chunksize %d' % (inputfile, outputfile, chunksize))

    # Processing    
    names = ['id', 'parent_id', 'content']
    for chunk in pd.read_csv(inputfile, header=None, names=names, chunksize=chunksize):
        process(chunk, outputfile)


if __name__ == "__main__":
   main(sys.argv[1:])
   