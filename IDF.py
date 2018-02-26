
class cal_IDF:
    def __init__(self, term, Corpus): ## We are taking 4 corpuses - WikiDump, AristoMini, Science_textbook and Flashcards
        self.corpus=Corpus
        self.term=term
    

    def add_term(self,term):
        self.corpus()