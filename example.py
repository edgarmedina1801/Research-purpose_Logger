import rlog_creator as rlog
from importlib import reload;reload(rlog) # not import for python2

import configuration.config1 as c1
import configuration.config2 as c2

import numpy as np
import cv2
import os

def Test():
    print('This is a simple test 50000 iterations (take around 20 seconds)')
    print('you should interrupt this proccess to save a partial processing.')
    for i in range(c1.iteration):
        a = np.ones([100,100])**-5 + c2.configuration9
    print("finished...")


Dataset = '/relative/path/to/read/detection.dod'
test_acc = np.random.rand()*100
det_num = np.random.randint(1000)
anchors = np.random.randint(10)
tracking_enable = 'True'
name_file = "Xception_16layers"
num = "16"
name_to_save = "Xception.pth"
# Uncomment any other one
# dicts={'accuracy_to100':test_acc,'detections1':det_num,'anchors':anchors}
# dicts={'accuracy_to50':test_acc,'detections2':det_num,'othertracking':'OFF'}
# dicts={'accuracy':test_acc,'other':'enabled','uncomment_this':1}
dicts={'accuracy':test_acc,'detections':det_num,'tracking':tracking_enable,'anchors':anchors}

# for testing... Create a CSV file with all lists of losses and accuracies to do a plot later.
train_accs=[0,10,20]
test_accs=[0,10,20]
train_losses=[0,10,20]
test_losses=[0,10,20]
file={'train acc ' + name_file  +"_"+num:     train_accs,
        'test acc ' + name_file +"_"+num:     test_accs,
        'train loss '+ name_file+"_"+num:     train_losses,
        'test loss '+ name_file +"_"+num:     test_losses,
        }

interrump = ""
text=""
try:
    Test()
except:
    print("process interrupted...")
    text = " - training INTERRUPTED by a bug..." # in cases of interruption problems ctrl+c or bugs in codes.
    interrump = "problem in A12 and B13 - "
rlog.save_log(dicts=dicts, file=file, ShortName_in=interrump+name_to_save, ExperimentName_in=name_file+text, GeneralComments_in='')
# rlog.save_log(dicts=dicts,dataset_name_in=Dataset)