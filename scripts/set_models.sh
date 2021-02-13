#!/bin/bash

# Brewery: prediction of 1D protein structure annotations (https://github.com/mircare/Brewery)
# Email us at gianluca[dot]pollastri[at]ucd[dot]ie if you wish to use it for purposes not permitted by the CC BY-NC-SA 4.0.

# set absolute paths for all model files required by Brewery

# SS3
echo `ls Predict_BRNN/models/SS3/*v7|wc -w` > Predict_BRNN/models/modelv7_ss3
ls Predict_BRNN/models/SS3/*v7 >> Predict_BRNN/models/modelv7_ss3
echo `ls Predict_BRNN/models/SS3/*v8|wc -w` > Predict_BRNN/models/modelv8_ss3
ls Predict_BRNN/models/SS3/*v8 >> Predict_BRNN/models/modelv8_ss3
echo `ls Predict_BRNN/models/SS3/*v9|wc -w` > Predict_BRNN/models/modelv9_ss3
ls Predict_BRNN/models/SS3/*v9 >> Predict_BRNN/models/modelv9_ss3

echo `ls Predict_BRNN/models/SS3/*vPSI+HH|wc -w` > Predict_BRNN/models/modelv78_ss3
ls Predict_BRNN/models/SS3/*vPSI+HH >> Predict_BRNN/models/modelv78_ss3
echo `ls Predict_BRNN/models/SS3/*vHH+BFD|wc -w` > Predict_BRNN/models/modelv89_ss3
ls Predict_BRNN/models/SS3/*vHH+BFD >> Predict_BRNN/models/modelv89_ss3

# SS8
echo `ls Predict_BRNN/models/SS8/*v7 |wc -w` > Predict_BRNN/models/modelv7_ss8
ls Predict_BRNN/models/SS8/*v7 >> Predict_BRNN/models/modelv7_ss8
echo `ls Predict_BRNN/models/SS8/*v8 |wc -w` > Predict_BRNN/models/modelv8_ss8
ls Predict_BRNN/models/SS8/*v8 >> Predict_BRNN/models/modelv8_ss8
echo `ls Predict_BRNN/models/SS8/*v9|wc -w` > Predict_BRNN/models/modelv9_ss8
ls Predict_BRNN/models/SS8/*v9 >> Predict_BRNN/models/modelv9_ss8

echo `ls Predict_BRNN/models/SS8/*_PSI+HH |wc -w` > Predict_BRNN/models/modelv78_ss8
ls Predict_BRNN/models/SS8/*_PSI+HH >> Predict_BRNN/models/modelv78_ss8
echo `ls Predict_BRNN/models/SS8/*_HH+BFD|wc -w` > Predict_BRNN/models/modelv89_ss8
ls Predict_BRNN/models/SS8/*_HH+BFD >> Predict_BRNN/models/modelv89_ss8

# TA14
echo `ls Predict_BRNN/models/TA14/ | grep -v "+"| wc -w` > Predict_BRNN/models/modelv22_ta14
ls Predict_BRNN/models/TA14/* | grep -v "+" >> Predict_BRNN/models/modelv22_ta14
echo `ls Predict_BRNN/models/TA14/ | grep "+" | wc -w` > Predict_BRNN/models/modelv44_ta14
ls Predict_BRNN/models/TA14/* | grep "+" >> Predict_BRNN/models/modelv44_ta14

# SA4
echo `ls Predict_BRNN/models/SA4/ | grep -v "+" | wc -w` > Predict_BRNN/models/modelv23_sa4
ls Predict_BRNN/models/SA4/* | grep -v "+" >> Predict_BRNN/models/modelv23_sa4
echo `ls Predict_BRNN/models/SA4/ | grep "+" | wc -w` > Predict_BRNN/models/modelv45_sa4
ls Predict_BRNN/models/SA4/* | grep "+" >> Predict_BRNN/models/modelv45_sa4

# CD4
echo `ls Predict_BRNN/models/CD4/ | grep -v "+" | wc -w` > Predict_BRNN/models/modelv22_cd4
ls Predict_BRNN/models/CD4/* | grep -v "+" >> Predict_BRNN/models/modelv22_cd4
echo `ls Predict_BRNN/models/CD4/ | grep "+" | wc -w` > Predict_BRNN/models/modelv44_cd4
ls Predict_BRNN/models/CD4/* | grep "+" >> Predict_BRNN/models/modelv44_cd4

abs_path=`pwd`
sed -i'' -e "s|Predict_BRNN/models|$abs_path\/Predict_BRNN/models|g" Predict_BRNN/models/modelv*
cd ../../
