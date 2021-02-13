[![PWC](https://camo.githubusercontent.com/6887feb0136db5156c4f4146e3dd2681d06d9c75/68747470733a2f2f692e6372656174697665636f6d6d6f6e732e6f72672f6c2f62792d6e632d73612f342e302f38387833312e706e67)](https://github.com/mircare/Brewery/#license)

# Microbrewery: profile-less prediction of 1D protein structure annotations

The docker container is available at https://hub.docker.com/r/mircare/microbrewery ([HOWTO](https://github.com/mircare/microbrewery#use-the-docker-image)).  

See https://github.com/mircare/Brewery for profile-based prediction of protein structure annotations.

## Setup
```
$ git clone https://github.com/mircare/Microbrewery/ --depth 1 && rm -rf Microbrewery/.git
```

### Requirements
1. Python3 (https://www.python.org/downloads/);
1. NumPy (https://www.scipy.org/scipylib/download.html);


## How to run Microbrewery
```
$ python3 Microbrewery/Microbrewery.py -i Microbrewery/example/2FLGA.fasta --cpu 4 
```

### How to run Microbrewery on multiple sequences
```
# To split a FASTA file with multiple sequences (Optionally)
$ python3 Microbrewery/split_fasta.py many_sequences.fasta

# To predict all the fasta files in a given directory (Fastas)
$ python3 Microbrewery/multiple_fasta.py -i Fastas/ --cpu 4 --fast
```

## How to visualize the help of Microbrewery
```
$ python3 Microbrewery/Microbrewery.py --help
usage: Microbrewery.py [-h] [-input fasta_file] [--cpu CPU] [--fast] [--noSS]
                  [--noTA] [--noSA] [--noCD] [--distill] [--setup]

This is the standalone of Microbrewery5. Run it on a FASTA file to predict its
Secondary Structure in 3- and 8-classes (Porter5), Solvent Accessibility in 4
classes (PaleAle5), Torsional Angles in 14 classes (Porter+5) and Contact
Density in 4 classes (BrownAle).

optional arguments:
  -h, --help         show this help message and exit
  -input fasta_file  FASTA file containing the protein to predict
  --cpu CPU          How many cores to perform this prediction
  --fast             Use only HHblits (skip PSI-BLAST)
  --bfd              Harness also the BFD database (https://bfd.mmseqs.com/)
  --noSS             Skip Secondary Structure prediction with Porter5
  --noTA             Skip Torsional Angles prediction with Porter+5
  --noSA             Skip Solvent Accessibility prediction with PaleAle5
  --noCD             Skip Contact Density prediction with BrownAle5
  --distill          Generate useful outputs for 3D protein structure prediction
  --setup            Initialize Microbrewery from scratch (it is recommended when
                     there has been any change involving PSI-BLAST, HHblits,
                     Microbrewery itself, etc).

E.g., run Microbrewery on 4 cores: python3 Microbrewery.py -i example/2FLGA --cpu 4
```

### Use the docker image
```
# Set the absolute PATHs for databases and query sequences (stored locally)
$ docker run --name microbrewery -v /**PATH_to_fasta_to_predict**:/Microbrewery/query \
--cap-add IPC_LOCK mircare/microbrewery sleep infinity &


## Citation
If you use Microbrewery, please cite our Bioinformatics paper:
```
@article{torrisi_brewery_2020,
	title = {Brewery: Deep Learning and deeper profiles for the prediction of 1D protein structure annotations},
	doi = {10.1093/bioinformatics/btaa204},
	journal = {Bioinformatics},
	author = {Torrisi, Mirko and Pollastri, Gianluca}
}
```


## References
Brewery: Deep Learning and deeper profiles for the prediction of 1D protein structure annotations,<br>
Bioinformatics, Oxford University Press; Mirko Torrisi and Gianluca Pollastri;<br>
Guest link: https://academic.oup.com/bioinformatics/advance-article/doi/10.1093/bioinformatics/btaa204/5811232?guestAccessKey=9a73ae2a-2cb6-4fe1-b333-a4f3261f02cf.

Protein Structure Annotations; Essentials of Bioinformatics, Volume I. Springer Nature<br>
Mirko Torrisi and Gianluca Pollastri; doi: https://doi.org/10.1007/978-3-030-02634-9_10.


## License
This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

Email us at gianluca[dot]pollastri[at]ucd[dot]ie if you wish to use it for purposes not permitted by the CC BY-NC-SA 4.0.

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a>
