

class cal_IDF:
    def __init__(self, dict, num_doc): ## We are taking 4 corpuses - WikiDump, AristoMini, Science_textbook and Flashcards
        self.dict1=dict
        self.num_doc=num_doc
    def get_IDF(self):
        for key1 in self.dict1.keys():
            self.dict1[key1]=self.dict1[key1]/float(self.num_doc)