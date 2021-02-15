[![PWC](https://camo.githubusercontent.com/6887feb0136db5156c4f4146e3dd2681d06d9c75/68747470733a2f2f692e6372656174697665636f6d6d6f6e732e6f72672f6c2f62792d6e632d73612f342e302f38387833312e706e67)](https://github.com/mircare/Brewery/#license)

# Microbrewery: Deep Transfer Learning for alignment-free prediction of protein structure annotations

The docker container is available at https://hub.docker.com/r/mircare/microbrewery ([HOWTO](https://github.com/mircare/microbrewery#use-the-docker-image)).  

See https://github.com/mircare/Brewery for profile-based prediction of protein structure annotations.

## Setup
```
$ git clone https://github.com/mircare/Microbrewery/ --depth 1 && rm -rf Microbrewery/.git
```

### Requirements
1. Python3 (https://www.python.org/downloads/);
1. NumPy (https://www.scipy.org/scipylib/download.html);


## Run Microbrewery
```
$ python3 Microbrewery/Microbrewery.py -i Microbrewery/example/2FLGA.fasta --cpu 4 
```

### Run Microbrewery on multiple sequences
```
# To split a FASTA file containing multiple sequences
$ python3 Microbrewery/split_fasta.py many_sequences.fasta

# To predict all the fasta files in a given directory, e.g. DIRNAME
$ python3 Microbrewery/multiple_fasta.py -i DIRNAME/ --cpu 4 --fast
```

## The help of Microbrewery
```
$ python3 Microbrewery/Microbrewery.py --help
usage: Microbrewery.py [-h] [-input fasta_file] [--noSS] [--noTA] [--noSA]
                       [--noCD] [--setup]

This is the standalone of Microbrewery. Run it on a FASTA file to predict its
Secondary Structure in 3- and 8-classes (Porter5), Solvent Accessibility in 4
classes (PaleAle5), Structural Motifs in 14 classes (Porter+5) and Contact
Density in 4 classes (BrownAle5).

optional arguments:
  -h, --help         show this help message and exit
  -input fasta_file  FASTA file containing the protein to predict
  --noSS             Skip Secondary Structure prediction
  --noTA             Skip Structural Motifs prediction
  --noSA             Skip Solvent Accessibility prediction
  --noCD             Skip Contact Density prediction
  --setup            Initialize Microbrewery from scratch (e.g., required when
                     it is moved).

E.g., python3 Microbrewery.py -i example/2FLGA.fasta
```

### Use the docker image
```
# Set the absolute PATHs to the query sequences
$ docker run --name microbrewery -v /**PATH_to_fasta_to_predict**:/Microbrewery/query \
--cap-add IPC_LOCK mircare/microbrewery sleep infinity &

# Run Microbrewery
$ docker exec microbrewery python3 Microbrewery.py -i query/2FLGA.fasta
```

## Performances on the 2019_test set of 618 proteins
| Method | SS3 | SS8 | TA14 | CD4 |
| :--- | :---: | :---: | :---: | :---: |
| Microbrewery | 72.6% | 59.2% | 54.8% | 36.8% |51.7%|
| SPIDER3-single | 71.4% | 57.6% | 50.9% | 32.5% | N/A |


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
Mirko Torrisi and Gianluca Pollastri; Post-print: https://www.researchgate.net/publication/332048741_Protein_Structure_Annotations.

Deeper Profiles and Cascaded Recurrent and Convolutional Neural Networks for state-of-the-art Protein Secondary Structure Prediction, Scientific Reports, Nature Publishing Group; Mirko Torrisi, Manaz Kaleel and Gianluca Pollastri;<br>
doi: https://doi.org/10.1038/s41598-019-48786-x.

PaleAle 5.0: prediction of protein relative solvent accessibility by deep learning, Amino Acids, Springer<br>
Manaz Kaleel, Mirko Torrisi, Catherine Mooney and Gianluca Pollastri; Guest Link: https://rdcu.be/bNlXS.


## License
This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

Email us at gianluca[dot]pollastri[at]ucd[dot]ie if you wish to use it for purposes not permitted by the CC BY-NC-SA 4.0.

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a>
