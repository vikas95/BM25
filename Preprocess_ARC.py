import csv

class Preprocess_Arc:
    def __init__(self, ARC, directory):
        self.corpus_name=ARC
        self.directory=directory
        self.col_size=[]

    def preprocess(self):
        if self.corpus_name == "ARC":
            file1=open(self.directory,"r")
            for line in file1:
                cols=line.split(", ")
                self.col_size.append(len(cols))

            return set(self.col_size)

