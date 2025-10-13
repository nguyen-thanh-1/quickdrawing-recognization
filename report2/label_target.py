import os
import pandas as pd

data = r"D:\private\FPTU\FA25\DPL302m\data"
labels = []
filepaths = []
folds = os.listdir(data)

for fold in folds:
    fpath = os.path.join(data, fold)
    flist = os.listdir(fpath)

    for f in flist:
        fullpath = os.path.join(fpath, f)
        filepaths.append(fullpath)

        if fold == "apple":
            labels.append("Apple")
        elif fold == "circle":
            labels.append("Circle")
        elif fold == "cloud":
            labels.append("Cloud")
        elif fold == "cup":
            labels.append("Cup")
        elif fold == "diamond":
            labels.append("Diamond")
        elif fold == "fish":
            labels.append("Fish")
        elif fold == "guitar":
            labels.append("Guitar")
        elif fold == "hat":
            labels.append("Hat")
        elif fold == "headphones":
            labels.append("Headphones")
        elif fold == "laptop":
            labels.append("Laptop")
        elif fold == "moon":
            labels.append("Moon")
        elif fold == "pants":
            labels.append("Pants")
        elif fold == "pencil":
            labels.append("Pencil")
        elif fold == "rectangle":
            labels.append("Rectangle")
        elif fold == "shirt":
            labels.append("Shirt")
        elif fold == "shock":
            labels.append("Shock")
        elif fold == "soccer_ball":
            labels.append("Soccer Ball")
        elif fold == "sun":
            labels.append("Sun")
        elif fold == "watermelon":
            labels.append("Watermelon")
        elif fold == "triangle":
            labels.append("Triangle")
        else:
            labels.append("Wine glass")

pic_count = len(filepaths)
labels_count = len(set(labels))

print(f"Có {labels_count} labels: ")
print(set(labels))
print(f"Có {pic_count} tấm: ")
print(filepaths) # -> 21 cat with each is 75 ->> 1575 pics

Fseries = pd.Series(filepaths, name= 'filepaths')
Lseries = pd.Series(labels, name='label')
df = pd.concat([Fseries, Lseries], axis= 1)

print(df.to_string())