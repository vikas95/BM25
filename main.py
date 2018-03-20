from Word_segment import parse_documents
from IDF import cal_IDF

lines=parse_documents("Aristo","Aristo_mini/")
posting_list,TF, num_doc = lines.parse_doc()
IDF=cal_IDF(TF,num_doc).get_IDF()
print (len(posting_list),len(TF))
print(TF)

