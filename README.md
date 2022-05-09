# Android Screenshot Ransomware Detector

## Project Background and Rationale

Technological applications hosted on Android operated devices are highly vulnerable to these ransomware attacks for data collection. 
Identifying which of these Android Applications deliver the ransomware attacks will greatly help reduce the number of victimized devices
and leaks of information. The process of identification is very tedious and time consuming for a team of highly educated employees to do,
therefore programs have been built to automate the process in an efficient and quicker method.

This project focuses on a program that will detect whether an application is classified as ransomware or benign based on the images of the 
application or screenshots of the threatening message. The program or tool we used is a Convolutional Neural Network (CNN) that will allow
us to set certain parameters and classifiers to help distinguish between ransomware and benign images.
    
## Data Set Details
The dataset used to train and test this model is a hand-selected sample of images retrieved from Google Images. 
Unfortunately, there is no free dataset that met the requirements needed for this datamodel, resulting in a fairly limited hand-selected
dataset.

### Data Set Classification Statistics
* Total Images: 870
* Ransomware Images: 327
* Benign Images: 543

## How to Use
1. Place your raw data files (ideally either PNG or JPG formats) in two folders, `input_class_benign` and `input_class_ransomware` depending on its class
2. Run `remove-duplicates .input_class_benign`
3. Run `remove-duplicates .input_class_ransomware`
4. Run `file-prep-py`
5. Run `main.py`

After completing these steps, the model will be exported as `weights-Test-CNN.hdf5` and the test results will be displayed on your screen

## Files in this Repo:

### remove-duplicates.py
Helper function that will read the raw data, and delete two files if they are identical. 

### file-prep.py
Cleans up de-duplicated data to be in the correct file format and naming convention.

Will convert files to JPG if currently saved as JPEG or JFIF, and rename the file to be either ransomware-#### or benign-####

### model-prediction.py
A debug file that will display the result of testing a particulr file, or series of files.

### main.py
The file responsible for taking the cleaned up data, converting to black/white, resizing, and then training and testing the model using Keras.
