# Microbrewery: prediction of 1D protein structure annotations (https://github.com/mircare/Microbrewery)
# Email us at gianluca[dot]pollastri[at]ucd[dot]ie if you wish to use it for purposes not permitted by the CC BY-NC-SA 4.0.

# Usage: python3 multiple_fasta.py -i Fastas/ --cpu 4
# (run 4 parallel instances of Microbrewery on 4 cores)

import os, sys
import argparse, time
from multiprocessing import Pool

### parallel code ##
def loop(line):
    os.system('python3 %s -i %s' % (executable, line))

### set argparse
parser = argparse.ArgumentParser(description="This is the standalone of Microbrewery for multiple inputs. It is sufficient to specify a directory containing FASTA files to start the prediction of the respective structural annotations.", 
epilog="E.g., to run 2 instances of Micobrewery in parallel: python3 multiple_fasta.py -i Fastas/ --cpu 4")
parser.add_argument("-i", type=str, nargs=1, help="Indicate the directory containing the FASTA files.")
parser.add_argument("--cpu", type=int, default=1, help="Specify how many cores to use.")
parser.add_argument("--noLOG", help="Skip most of the logs.", action="store_true")
parser.add_argument("--noSS", help="Skip Secondary Structure prediction with Porter5", action="store_true")
parser.add_argument("--noTA", help="Skip Torsional Angles prediction with Porter+5", action="store_true")
parser.add_argument("--noSA", help="Skip Solvent Accessibility prediction with PaleAle5", action="store_true")
parser.add_argument("--noCD", help="Skip Contact Density prediction with BrownAle5", action="store_true")
parser.add_argument("--setup", help="Initialize Microbrewery from scratch (e.g., required when it is moved).", action="store_true")
args = parser.parse_args()

## check arguments
if not args.i:
    print("Usage: python3 "+sys.argv[0]+" -i <fasta_dir> [--cpu CPU_number]\n--help for the full list of commands")
    exit()

#initialization variables
executable = os.path.abspath(os.path.dirname(sys.argv[0]))+"/Microbrewery.py"
if not os.path.isfile(executable):
    print("\n---->>No executable retrieved at", executable)
    exit()

if not os.path.isdir("".join(args.i)):
    print("\n---->>","".join(args.i),"isn't a directory! Please consider running split_fasta.py.")
    exit()

if not os.path.isfile(os.path.abspath(os.path.dirname(sys.argv[0]))+"/scripts/Predict_BRNN/models/modelv7_ss3") or args.setup:
    os.system("python3 %s --setup" % executable)

# fetch all the inputs from the passed directory, and sort them by size
os.chdir("".join(args.i))
sorted_files = sorted(os.listdir(os.getcwd()), key = os.path.getsize, reverse=True)

if args.noSS:
    sorted_files = [line + " --noSS" for line in sorted_files]
if args.noTA:
    sorted_files = [line + " --noTA" for line in sorted_files]
if args.noSA:
    sorted_files = [line + " --noSA" for line in sorted_files]
if args.noCD:
    sorted_files = [line + " --noCD" for line in sorted_files]
if args.noLOG:
    sorted_files = [line + " > /dev/null" for line in sorted_files]

# ligth the bomb // launch the parallel code
time0 = time.time()
with Pool(args.cpu) as p:
    p.map(loop, sorted_files, 1)

print("Microbrewery predicted %d proteins in %.2fs (%.2fs per protein)" % (len(sorted_files),time.time()-time0, (time.time()-time0)/len(sorted_files)))
