# Brewery
### state-of-the-art ab initio prediction of 1D protein structure annotations 

The web server of Brewery is available at http://distilldeep.ucd.ie/brewery/.  
The train and test sets are available at http://distilldeep.ucd.ie/brewery/data/.


### Reference
Porter 5: fast, state-of-the-art ab initio prediction of protein secondary structure in 3 and 8 classes<br>
Mirko Torrisi, Manaz Kaleel and Gianluca Pollastri; bioRxiv 289033; doi: https://doi.org/10.1101/289033.


## Setup
```
$ git clone https://github.com/mircare/Brewery/
```

### Requirements
1. Python3 (https://www.python.org/downloads/);
1. NumPy (https://www.scipy.org/scipylib/download.html);
1. HHblits (https://github.com/soedinglab/hh-suite/);
1. uniprot20 (http://wwwuser.gwdg.de/~compbiol/data/hhsuite/databases/hhsuite_dbs/old-releases/uniprot20_2016_02.tgz).

#### Optionally (for more accurate predictions):
1. PSI-BLAST (ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/); 
1. UniRef90 (ftp://ftp.uniprot.org/pub/databases/uniprot/uniref/uniref90/uniref90.fasta.gz).


## How to run Brewery with/without PSI-BLAST
```
# To exploit HHblits only (for fast and accurate predictions)
$ python3 Brewery/Brewery.py -i Brewery/example/2FLGA.fasta --cpu 4 --fast

# To exploit both PSI-BLAST and HHblits (for very accurate predictions)
$ python3 Brewery/Porter5.py -i Brewery/example/2FLGA.fasta --cpu 4
```

## Performances of Secondary Structure Predictors in 3 classes
| Method | Q3 per AA | SOV per AA | Q3 per protein | SOV per protein |
| :--- | :---: | :---: | :---: | :---: |
| **Brewery** | **83.81%** | **83.29%** | **84.32%** | **84.57%** |
| SPIDER 3 | 83.15% | 82.04% | 83.42% | 83.17% |
| **Brewery *HHblits only*** | **83.06%** | **82.21%** | **83.68%** | **83.71%** |
| SSpro 5 *with templates* | 82.58% | 80.13% | 83.94% | 82.49% |
| PSIPRED 4.01 | 81.88% | 80.17% | 82.48% | 81.70% |
| RaptorX-Property | 81.86% | 81.86% | 82.57% | 83.13% |
| Porter 4 | 81.66% | 81.11% | 82.29% | 82.51% | 
| SSpro5 *ab initio* | 81.17% | 78.54% | 81.10% | 79.45% |
| DeepCNF | 81.04% | 80.84% | 81.16% | 81.46% |

Reference: Table 1 in https://doi.org/10.1101/289033.


## Performances of Secondary Structure Predictors in 8 classes
| Method | Q8 per AA | SOV per AA | Q8 per protein | SOV per protein |
| :--- | :---: | :---: | :---: | :---: |
| **Brewery** | **73.02%** | **76.83%** | **73.92%** | **77.67%** |
| SSpro 5 *with templates* | 71.91% | 78.55% | 74.46% | 77.84% |
| **Brewery *HHblits only*** | **71.8%** | **75.45%** | **72.83%** | **76.46%** |
| RaptorX-Property | 70.74% | 74.88% | 71.78% | 75.84% |
| SSpro5 *ab initio* | 68.85% | 72.26% | 69.27% | 73.06% |


## Performances of Solvent Accessibility Predictors in up to 4 classes
| Method | Q2 per AA | Q3 per AA | Q4 per AA |
| :--- | :---: | :---: | :---: |
| ACCpro 5 *with templates* | 80.5% | N.A. | N.A. |
| **Brewery** | **80.48%** | **66.41%** | **56.46%** |
| PaleAle 4 | 78.21% | N.A. | 52.53% |
| SPIDER 3 | 77.91% | 61.19% | 49.01% |
| ACCpro 5 *ab initio* | 76.6% | N.A. | N.A. |
| RaptorX-Property | N.A. | 63.25% | N.A. |


## Performances of Torsion Angles Predictors in 14 classes
| Method | Q14 per AA | SOV per AA | Q14 per protein | SOV per protein |
| :--- | :---: | :---: | :---: | :---: |
| **Brewery** | **69.93%** | **77.19%** | **70.59%** | **75.6%** |
| SPIDER 3 | 66.58% | 74.04% | 66.27% | 71.8% |
| Porter+ | 64.73% | 72.62% | 66% | 70.98% |


## Performances of Contact Density Predictors in 4 classes
| Method | Q4 per AA | Q4 per protein |
| :--- | :---: | :---: |
| **Brewery** | **50.01%** | **48%** |
| BrownAle | 46.5% | N.A. |


## License
This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

Email us at gianluca[dot]pollastri[at]ucd[dot]ie if you wish to use it for purposes not permitted by the CC BY-NC-SA 4.0.

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a>