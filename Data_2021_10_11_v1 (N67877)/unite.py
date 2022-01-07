import glob
import os

path = os.path.dirname(os.path.realpath(__file__))
os.chdir(path)

if os.path.exists("concatenate_texts.csv"):
    os.remove("concatenate_texts.csv")
else:
    print("The file does not exist")

read_files = glob.glob("*.csv")

print(read_files)

with open("concatenate_texts.csv", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())