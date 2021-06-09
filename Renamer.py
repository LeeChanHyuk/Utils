import os

# The folder path that i want to change
file_path = 'C:/Users/cjsgk/Desktop/Git/EfficientDet-Face_and_Eye/HelenDataset/trainimage'
file_names = os.listdir(file_path)
for name in file_names:
    src = os.path.join(file_path, name)
    # In this case, i want to delete '_' in my filename
    new_name = name.replace('_',"")
    new_name = os.path.join(file_path, new_name)
    os.rename(src, new_name)