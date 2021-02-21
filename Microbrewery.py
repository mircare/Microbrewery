# Microbrewery: prediction of 1D protein structure annotations (https://github.com/mircare/Microbrewery)
# Email us at gianluca[dot]pollastri[at]ucd[dot]ie if you wish to use Microbrewery for purposes not permitted by the CC BY-NC-SA 4.0.

import argparse
import os, sys
import time

## check Python version
if sys.version_info[0] < 3:
   print("Python2 detected, please use Python3.")
   exit()

### set argparse
parser = argparse.ArgumentParser(description="This is the standalone of Microbrewery. Run it on a FASTA file to predict its Secondary Structure in 3- and 8-classes (Porter5), Solvent Accessibility in 4 classes (PaleAle5), Structural Motifs in 14 classes (Porter+5) and Contact Density in 4 classes (BrownAle).",
epilog="E.g., python3 Microbrewery.py -i example/2FLGA.fasta")
parser.add_argument("-input", metavar='fasta_file', type=str, nargs=1, help="FASTA file containing the protein to predict")
# parser.add_argument("--cpu", type=int, default=1, help="How many cores to perform this prediction")
parser.add_argument("--noSS", help="Skip Secondary Structure prediction", action="store_true")
parser.add_argument("--noTA", help="Skip Structural Motifs prediction", action="store_true")
parser.add_argument("--noSA", help="Skip Solvent Accessibility prediction", action="store_true")
parser.add_argument("--noCD", help="Skip Contact Density prediction", action="store_true")
parser.add_argument("--setup", help="Initialize Microbrewery from scratch (e.g., required when it is moved).", action="store_true")
args = parser.parse_args()

path = os.path.dirname(os.path.abspath(sys.argv[0]))+"/scripts"
if args.setup or not os.path.isfile(path+"/Predict_BRNN/models/modelv7_ss3"):
    # compile predict and set absolute paths for all model files
    os.system('cd %s/Predict_BRNN; make -B; cd ..;bash set_models.sh; cd %s' % (path, path))
    
    print("\n>>>>> Setup completed successfully. If any problem occurs, please run \"python3 Microbrewery.py --setup\". <<<<<\n")

## check arguments
if not args.input:
    print("Usage: python3 "+sys.argv[0]+" -i <fasta_file>\n--help to display the help")
    exit()

# save protein path and name, and current PATH
filename = "".join(args.input)
predict = path+"/Predict_BRNN/Predict"
models = path+"/Predict_BRNN/models/"


print("~~~~~~~~~ Prediction of "+filename+" started ~~~~~~~~~")
time0 = time.time()

pid = []
aa = []
tmp = ""
with open(filename, "r") as fasta:
    for line in fasta.readlines():
        if ">" in line:
            pid.append(line.strip())
            aa.append(list(tmp))
            tmp = ""
        else:
            tmp += line.strip()
    aa.append(list(tmp))
aa.pop(0)

AA = {"A": "1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ",
    "C": "0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ",
    "D": "0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ",
    "E": "0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ",
    "F": "0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ",
    "G": "0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ",
    "H": "0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ",
    "I": "0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ",
    "K": "0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 ",
    "L": "0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 ",
    "M": "0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 ",
    "N": "0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 ",
    "P": "0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 ",
    "Q": "0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 ",
    "R": "0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 ",
    "S": "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 ",
    "T": "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 ",
    "V": "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 ",
    "W": "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 ",
    "Y": "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 ",
    "X": "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 "}

with open(filename+".ann22", "w") as ann22:
    with open(filename+".ann44", "w") as ann44:
        ann22.write(str(len(pid))+"\n")
        ann22.write("22 3\n")
        
        ann44.write(str(len(pid))+"\n")
        ann44.write("44 3\n")
        
        for i, line in enumerate(aa):
            ann22.write("pid"+str(i)+"\n"+str(len(line))+"\n")
            ann44.write("pid"+str(i)+"\n"+str(len(line))+"\n")
            
            for c in line:
                val = AA.get(c, "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 ")
                ann22.write(val)
                ann44.write(val+val)
            tmp = "0 " * len(line)
            ann22.write("\n"+tmp+"\n\n")
            ann44.write("\n"+tmp+"\n\n")



###############################################
############     SS prediction     ############
###############################################
if not args.noSS:
    ### predict SS in 3 classes
    time0SS = time.time()
    classes = 3
    os.system('tee %s.ann22_hh %s.ann22_bfd < %s.ann22 > /dev/null' % (filename, filename, filename))
    os.system('%s %smodelv7_ss3 %s.ann22 > /dev/null' % (predict, models, filename))
    os.system('%s %smodelv8_ss3 %s.ann22_hh > /dev/null' % (predict, models, filename))
    os.system('%s %smodelv9_ss3 %s.ann22_bfd > /dev/null' % (predict, models, filename))
    
    os.system('cp %s.ann44 %s.ann44_hhbfd ' % (filename, filename))
    os.system('%s %smodelv78_ss3 %s.ann44 > /dev/null' % (predict, models, filename))
    os.system('%s %smodelv89_ss3 %s.ann44_hhbfd > /dev/null' % (predict, models, filename))
    
    print('Secondary Structure in %d classes predicted in %.2fs' % (classes, (time.time()-time0SS)))

    ## ensemble predictions and process output
    toChar = {0 : "H", 1 : "E", 2 : "C"}
    prediction = open(filename+".ss3", "w")
    probsF22 = open(filename+".ann22.probsF", "r").readlines()
    probsF22_hh = open(filename+".ann22_hh.probsF", "r").readlines()
    probsF22_bfd = open(filename+".ann22_bfd.probsF", "r").readlines()

    probsF44 = open(filename+".ann44.probsF", "r").readlines()
    probsF44_hhbfd = open(filename+".ann44_hhbfd.probsF", "r").readlines()

    for i, id in enumerate(pid):
        prediction.write(id+"\n")
        prediction.write("#\tAA\tSS\tHelix\tSheet\tCoil\n")

        probs22 = list(map(float, probsF22[3+i*5].strip().split()))
        probs22_hh = list(map(float, probsF22_hh[3+i*5].strip().split()))
        probs22_bfd = list(map(float, probsF22_bfd[3+i*5].strip().split()))

        probs44 = list(map(float, probsF44[3+i*5].strip().split()))
        probs44_hhbfd = list(map(float, probsF44_hhbfd[3+i*5].strip().split()))

        for j in range(0, len(probs22), classes):
            tmp = [round((3*probs22[j+k]+3*probs22_hh[j+k]+3*probs22_bfd[j+k]+probs44[j+k]+probs44_hhbfd[j+k])/11, 4) for k in range(classes)]
            index = tmp.index(max(tmp))
            k = int(j/classes)
            prediction.write(str(k+1)+"\t"+aa[i][k]+"\t"+toChar[index]+"\t"+str(tmp[0])+"\t"+str(tmp[1])+"\t"+str(tmp[2])+"\n")
        prediction.write("\n\n")
    prediction.flush()

    
    ######## eight-state prediction ########
    def generate8statesANN(ann, preds):
        ann_ss3 = open(ann, "r").readlines()
        input_size = int(ann_ss3[1].split()[0])
        with open(ann+"+ss3", "w") as ann_ss8:
            ann_ss8.write(ann_ss3[0]+str(input_size+3)+" 8\n")

            for i in range(2, len(ann_ss3), 5):
                ann_ss8.write(ann_ss3[i]+ann_ss3[i+1])
                prob = preds[i+1].split()
                for j in range(int(ann_ss3[i+1])):
                    ann_ss8.write(ann_ss3[i+2][j*input_size*2:(j+1)*input_size*2]+" ".join(prob[j*3:j*3+3])+" ")
                ann_ss8.write("\n"+ann_ss3[i+3]+"\n")

    ### generate inputs and predict SS8
    time1SS = time.time()
    classes = 8
    generate8statesANN(filename+".ann22", probsF22)
    generate8statesANN(filename+".ann22_hh", probsF22_hh)
    generate8statesANN(filename+".ann22_bfd", probsF22_bfd)

    generate8statesANN(filename+".ann44", probsF44)
    generate8statesANN(filename+".ann44_hhbfd", probsF44_hhbfd)

    os.system('%s %smodelv7_ss8 %s.ann22+ss3 > /dev/null' % (predict, models, filename))
    os.system('%s %smodelv8_ss8 %s.ann22_hh+ss3 > /dev/null' % (predict, models, filename))
    os.system('%s %smodelv9_ss8 %s.ann22_bfd+ss3 > /dev/null' % (predict, models, filename))
    
    os.system('%s %smodelv78_ss8 %s.ann44+ss3 > /dev/null' % (predict, models, filename))
    os.system('%s %smodelv89_ss8 %s.ann44_hhbfd+ss3 > /dev/null' % (predict, models, filename))
    print('Secondary Structure in %d classes predicted in %.2fs' % (classes, (time.time()-time1SS)))

    ### ensemble SS predictions and process output
    toChar = {0 : "G", 1 : "H", 2 : "I", 3 : "E", 4 : "B", 5 : "C", 6 : "S", 7 : "T"}
    prediction = open(filename+".ss8", "w")
    probsF25 = open(filename+".ann22+ss3.probsF", "r").readlines()
    probsF25_hh = open(filename+".ann22_hh+ss3.probsF", "r").readlines()
    probsF25_bfd = open(filename+".ann22_bfd+ss3.probsF", "r").readlines()

    probsF47 = open(filename+".ann44+ss3.probsF", "r").readlines()
    probsF47_hhbfd = open(filename+".ann44_hhbfd+ss3.probsF", "r").readlines()

    for i, id in enumerate(pid):
        prediction.write(id+"\n")
        prediction.write("#\tAA\tSS\tG\tH\tI\tE\tB\tC\tS\tT\n")

        probs25 = list(map(float, probsF25[3+i*5].strip().split()))
        probs25_hh = list(map(float, probsF25_hh[3+i*5].strip().split()))
        probs25_bfd = list(map(float, probsF25_bfd[3+i*5].strip().split()))

        probs47 = list(map(float, probsF47[3+i*5].strip().split()))
        probs47_hhbfd = list(map(float, probsF47_hhbfd[3+i*5].strip().split()))

        for j in range(0, len(probs25), classes):
            tmp = [round((3*probs25[j+k]+3*probs25_hh[j+k]+3*probs25_bfd[j+k]+probs47[j+k]+probs47_hhbfd[j+k])/11, 4) for k in range(classes)]
            index = tmp.index(max(tmp))
            k = int(j/classes)
            prediction.write(str(k+1)+"\t"+aa[i][k]+"\t"+toChar[index]+"\t"+str(tmp[0])+"\t"+str(tmp[1])+\
                "\t"+str(tmp[2])+"\t"+str(tmp[3])+"\t"+str(tmp[4])+"\t"+str(tmp[5])+"\t"+str(tmp[6])+"\t"+str(tmp[7])+"\n")
        prediction.write("\n\n")
    prediction.close()


###############################################
############     TA prediction     ############
###############################################
if not args.noTA:
    ### predict TA in 14 classes
    time0TA = time.time()
    classes = 14
    os.system('sed -i "2s|.*|22 14|g" %s.ann22' % filename)
    os.system('sed -i "2s|.*|44 14|g" %s.ann44' % filename)
    os.system('%s %smodelv22_ta14 %s.ann22 > /dev/null' % (predict, models, filename))
    os.system('%s %smodelv44_ta14 %s.ann44 > /dev/null' % (predict, models, filename))
    
    print('Structural Motifs in %d classes predicted in %.2fs' % (classes, (time.time()-time0TA)))

    ### ensemble TA predictions and process output
    toChar = {0 : "b", 1 : "h", 2 : "H", 3 : "I", 4 : "C", 5 : "e", 6 : "E", 7 : "S", 8 : "t", 9 : "g", 10 : "T", 11 : "B", 12 : "s", 13 : "i"}
    prediction = open(filename+".ta14", "w")
    probsF22 = open(filename+".ann22.probsF", "r").readlines()
    probsF44 = open(filename+".ann44.probsF", "r").readlines()

    for i, id in enumerate(pid):
        prediction.write(id+"\n")
        prediction.write("#\tAA\tTA\tb\th\tH\tI\tC\te\tE\tS\tt\tg\tT\tB\ts\ti\n")

        probs22 = list(map(float, probsF22[3+i*5].strip().split()))
        probs44 = list(map(float, probsF44[3+i*5].strip().split()))

        for j in range(0, len(probs22), classes):
            tmp = [round((24*probs22[j+k]+16*probs44[j+k])/40, 4) for k in range(classes)]
            index = tmp.index(max(tmp))
            k = int(j/classes)
            prediction.write(str(k+1)+"\t"+aa[i][k]+"\t"+toChar[index]+"\t"+str(tmp[0])+"\t"+str(tmp[1])+\
                "\t"+str(tmp[2])+"\t"+str(tmp[3])+"\t"+str(tmp[4])+"\t"+str(tmp[5])+"\t"+str(tmp[6])+\
                "\t"+str(tmp[7])+"\t"+str(tmp[8])+"\t"+str(tmp[9])+"\t"+str(tmp[10])+"\t"+str(tmp[11])+\
                "\t"+str(tmp[12])+"\t"+str(tmp[13])+"\n")
        prediction.write("\n\n")
    prediction.close()

 
###############################################
############     SA prediction     ############
###############################################
if not args.noSA:
    ### predict SA in 4 classes
    time0SA = time.time()
    classes = 4
    
    ##add length
    def add_length(filename):
        ann22 = open(filename, "r").readlines()
        with open(filename+"+len", "w") as ann_sa:
            input_size = int(ann22[1].split()[0])
            ann_sa.write(ann22[0]+str(input_size+1)+" 4\n")
            
            for i in range(2, len(ann22), 5):
                length = int(ann22[i+1])
                ann_sa.write(ann22[i]+ann22[i+1])
                tmp = ann22[i+2].strip()+" "
                for j in range(0, len(tmp), input_size*2):
                    ann_sa.write(tmp[j:j+input_size*2]+str(length/1000)+" ")
                ann_sa.write("\n"+ann22[i+3]+"\n")

    add_length(filename+".ann22")
    add_length(filename+".ann44")
    os.system('%s %smodelv23_sa4 %s.ann22+len > /dev/null' % (predict, models, filename))
    os.system('%s %smodelv45_sa4 %s.ann44+len > /dev/null' % (predict, models, filename))
    
    print('Solvent Accessibility in %d classes predicted in %.2fs' % (classes, (time.time()-time0SA)))

    ### ensemble SA predictions and process output
    toChar = {0 : "B", 1 : "b", 2 : "e", 3 : "E"}
    prediction = open(filename+".sa4", "w")
    probsF23 = open(filename+".ann22+len.probsF", "r").readlines()
    probsF45 = open(filename+".ann44+len.probsF", "r").readlines()

    for i, id in enumerate(pid):
        prediction.write(id+"\n")
        prediction.write("#\tAA\tSA\tB\tb\te\tE\n")

        probs23 = list(map(float, probsF23[3+i*5].strip().split()))
        probs45 = list(map(float, probsF45[3+i*5].strip().split()))

        for j in range(0, len(probs23), classes):
            tmp = [round((9*probs23[j+k]+2*probs45[j+k])/11, 4) for k in range(classes)]
            index = tmp.index(max(tmp))
            k = int(j/classes)
            prediction.write(str(k+1)+"\t"+aa[i][k]+"\t"+toChar[index]+"\t"+str(tmp[0])+"\t"+str(tmp[1])+\
                "\t"+str(tmp[2])+"\t"+str(tmp[3])+"\n")
        prediction.write("\n\n")
    prediction.close()


###############################################
############     CD prediction     ############
###############################################
if not args.noCD:
    ### predict CD in 4 classes
    time0CD = time.time()
    classes = 4
    os.system('sed -i "2s|.*|22 4|g" %s.ann22' % filename)
    os.system('sed -i "2s|.*|44 4|g" %s.ann44' % filename)
    os.system('%s %smodelv22_cd4 %s.ann22 > /dev/null' % (predict, models, filename))
    os.system('%s %smodelv44_cd4 %s.ann44 > /dev/null' % (predict, models, filename))
    
    print('Contact Density in %d classes predicted in %.2fs' % (classes, (time.time()-time0CD)))

    ### ensemble CD predictions and process output
    toChar = {0 : "N", 1 : "n", 2 : "c", 3 : "C"}
    prediction = open(filename+".cd4", "w")
    probsF22 = open(filename+".ann22.probsF", "r").readlines()
    probsF44 = open(filename+".ann44.probsF", "r").readlines()

    for i, id in enumerate(pid):
        prediction.write(id+"\n")
        prediction.write("#\tAA\tCD\tN\tn\tc\tC\n")

        probs22 = list(map(float, probsF22[3+i*5].strip().split()))
        probs44 = list(map(float, probsF44[3+i*5].strip().split()))

        for j in range(0, len(probs22), classes):
            tmp = [round((9*probs22[j+k]+2*probs44[j+k])/11, 4) for k in range(classes)]
            index = tmp.index(max(tmp))
            k = int(j/classes)
            prediction.write(str(k+1)+"\t"+aa[i][k]+"\t"+toChar[index]+"\t"+str(tmp[0])+"\t"+str(tmp[1])+
                "\t"+str(tmp[2])+"\t"+str(tmp[3])+"\n")
        prediction.write("\n\n")
    prediction.close()
    

# end
timeEND = time.time()
print('Microbrewery predicted %s in %.2fs (TOTAL)' % (filename, timeEND-time0))

### remove all the temporary files
os.system('rm %s.ann22* %s.ann44* 2> /dev/null' % (filename, filename))
