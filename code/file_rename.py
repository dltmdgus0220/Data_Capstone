import os
import re


root = "/root/leewj/Figshare_all_Aug_resize/masks/0"

items1 = [item for item in filter(lambda item: re.search("^[0-9]+_mask_meningioma.png$", item), os.listdir(root))]
items2 = [item for item in filter(lambda item: re.search("^[0-9]+_mask_aug_meningioma.png$", item), os.listdir(root))]
items3 = [item for item in filter(lambda item: re.search("^[0-9]+_mask_glioma.png$", item), os.listdir(root))]
items4 = [item for item in filter(lambda item: re.search("^[0-9]+_mask_pituitary.png$", item), os.listdir(root))]
items5 = [item for item in filter(lambda item: re.search("^[0-9]+_mask_aug_pituitary.png$", item), os.listdir(root))]

img_split = []
for i in items1:
    img_split.append(i.split("_"))

for j in img_split:
    if len(j) == 4:
        file_oldname = os.path.join(root, j[0] + "_" + j[1] + "_" + j[2] + "_" + j[3])
        file_newname = os.path.join(root, j[0] + "_" + j[2] + "_" + j[3])
    elif len(j) == 3:
        file_oldname = os.path.join(root, j[0] + "_" + j[1] + "_" + j[2])
        file_newname = os.path.join(root, j[0] + "_" + j[2])
    os.rename(file_oldname, file_newname)

img_split = []
for i in items2:
    img_split.append(i.split("_"))

for j in img_split:
    if len(j) == 4:
        file_oldname = os.path.join(root, j[0] + "_" + j[1] + "_" + j[2] + "_" + j[3])
        file_newname = os.path.join(root, j[0] + "_" + j[2] + "_" + j[3])
    elif len(j) == 3:
        file_oldname = os.path.join(root, j[0] + "_" + j[1] + "_" + j[2])
        file_newname = os.path.join(root, j[0] + "_" + j[2])
    os.rename(file_oldname, file_newname)

img_split = []
for i in items3:
    img_split.append(i.split("_"))

for j in img_split:
    if len(j) == 4:
        file_oldname = os.path.join(root, j[0] + "_" + j[1] + "_" + j[2] + "_" + j[3])
        file_newname = os.path.join(root, j[0] + "_" + j[2] + "_" + j[3])
    elif len(j) == 3:
        file_oldname = os.path.join(root, j[0] + "_" + j[1] + "_" + j[2])
        file_newname = os.path.join(root, j[0] + "_" + j[2])
    os.rename(file_oldname, file_newname)

img_split = []
for i in items4:
    img_split.append(i.split("_"))

for j in img_split:
    if len(j) == 4:
        file_oldname = os.path.join(root, j[0] + "_" + j[1] + "_" + j[2] + "_" + j[3])
        file_newname = os.path.join(root, j[0] + "_" + j[2] + "_" + j[3])
    elif len(j) == 3:
        file_oldname = os.path.join(root, j[0] + "_" + j[1] + "_" + j[2])
        file_newname = os.path.join(root, j[0] + "_" + j[2])
    os.rename(file_oldname, file_newname)

img_split = []
for i in items5:
    img_split.append(i.split("_"))

for j in img_split:
    if len(j) == 4:
        file_oldname = os.path.join(root, j[0] + "_" + j[1] + "_" + j[2] + "_" + j[3])
        file_newname = os.path.join(root, j[0] + "_" + j[2] + "_" + j[3])
    elif len(j) == 3:
        file_oldname = os.path.join(root, j[0] + "_" + j[1] + "_" + j[2])
        file_newname = os.path.join(root, j[0] + "_" + j[2])
    os.rename(file_oldname, file_newname)