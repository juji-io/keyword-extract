
from pke.unsupervised import YAKE

import sys, getopt

def main(argv):

    inputfile = ''
    outputfile = ''
    topn = 20

    try:
        opts, args = getopt.getopt(argv,"hi:o:n:",["ifile=","ofile=","topn="])
    except getopt.GetoptError:
        print('extract.py -i <inputfile> -o <outputfile> -n <topn>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('extract.py -i <inputfile> -o <outputfile> -n <topn>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-n", "--topn"):
            topn = int(arg)

    with open(inputfile, "r") as f:
        document = f.read()

    extractor = YAKE()

    extractor.load_document(input=document,
                            language='en',
                            normalization=None)

    extractor.candidate_selection(n=3)

    extractor.candidate_weighting(window=3, use_stems=False)

    key_phrases = extractor.get_n_best(n=topn, threshold=0.8)

    with open(outputfile, "w") as f:
        for (keyphrase, score) in key_phrases:
            f.write(keyphrase)
            f.write('\n')

if __name__ == "__main__":
   main(sys.argv[1:])
