from Word_segment import parse_documents
from IDF import cal_IDF
from Preprocess_ARC import Preprocess_Arc
"""
# lines=parse_documents("Aristo","Aristo_mini/")
lines=parse_documents("ARC","ARC_corpus/")
posting_list,TF, num_doc = lines.parse_doc()
IDF=cal_IDF(TF,num_doc).get_IDF()
print (len(posting_list),len(TF))
print(TF)

"""

cols_sizes, questions, candidates, algebra=Preprocess_Arc("ARC","ARC_corpus/ARC-Challenge/ARC-Challenge-Train.csv").preprocess()

print (len(algebra))
