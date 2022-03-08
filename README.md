# Extract Keywords

## Setup

You will need python 3.

```Shell
pip3 install git+https://github.com/boudinfl/pke.git
python3  -m spacy download en_core_web_sm
```

## Run extraction

Run `extract.py` script to extract. For example:

```Shell
python3 extract.py -i surface-area-reactangular-prism.txt -o output.csv -n 20
```

You can change the following arguments:

* `-i` input file name.
* `-o` output file name.
* `-n` the number of keywords desired
