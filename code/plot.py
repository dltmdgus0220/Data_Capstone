import os
from glob import glob
import csv
import pandas as pd
import matplotlib.pyplot as plt

def read_csv(path):
    list = []
    f = open(path, 'r')
    rd = csv.reader(f)
    for line in rd:
        list.append(line)
    f.close()
    return list[1:]

paths = '/root/vol1/da_capstone/pytorch-nested-unet-master/models/Figshare*/log.csv' # log.csv 파일이 저장된 경로 설정
paths = glob(paths)


model_list = pd.DataFrame(read_csv(paths[0]))
train_loss = model_list[:][2].astype(float)
train_iou = model_list[:][3].astype(float)
val_loss = model_list[:][4].astype(float)
val_iou = model_list[:][5].astype(float)
list = [train_loss, val_loss, train_iou, val_iou]
        
for i in range(1,5,2):
    plt.subplot(2, 1, i//2 + 1) 
    plt.ylim(0, 1.25)
    plt.yticks([0,0.25,0.5,0.75,1])
    plt.xlabel('epoch')
    plt.title("train & validation")
    if(i == 1):
        plt.ylabel('loss')
    else:
        plt.ylabel('iou')
    plt.plot(list[i-1].values.tolist(), label = 'train')
    plt.plot(list[i].values.tolist(), label = 'validation')
    plt.legend()

plt.suptitle("  UNet++(deepsupervision)  lr = 0.005", fontsize = 20)
plt.tight_layout()
plt.savefig("/root/vol1/da_capstone/pytorch-nested-unet-master/outputs/savefig_NestedUNet_deepsupervision(0.005,100).png")