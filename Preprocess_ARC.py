import csv
count=0
lens=[]
"""
with open('ARC_corpus/ARC-Challenge/ARC-Challenge-Dev.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        count+=1
        lens.append(len(row))


print (set(lens))
"""

class Preprocess_Arc:
    def __init__(self, ARC, directory):
        self.corpus_name=ARC
        self.directory=directory
        self.col_size=[]
        self.question=[]
        self.candidates=[]
        self.algebra_question=[]

    def preprocess(self):
        if self.corpus_name == "ARC":
            """
            file1=open(self.directory,"r")
            for line in file1:
                cols=line.split(", ")
                self.col_size.append(len(cols))
            """
            with open(self.directory, newline='') as f:
                reader = csv.reader(f)
                count=0
                for row in reader:
                    count += 1
                    if count==1:
                       pass
                    else:

                        print (count)

                        self.col_size.append(len(row))
                        question_ans=row[9]
                        offset=3
                        int_count=0 ## number of numerals in the question
                        for w1 in question_ans.split():
                            if w1.isdigit():
                               int_count+=1
                        if int_count>1:
                           self.algebra_question.append(question_ans)

                        if "(A)" in question_ans:
                            A_index = question_ans.index("(A)")
                            B_index = question_ans.index("(B)")
                            C_index = question_ans.index("(C)")
                            if "(D)" in question_ans:
                                D_index = question_ans.index("(D)")
                                self.candidates.append([question_ans[A_index + offset:B_index - 1], question_ans[B_index + offset:C_index - 1],
                                     question_ans[C_index + offset:D_index - 1], question_ans[D_index + offset:]])
                            else:
                                self.candidates.append([question_ans[A_index + offset:B_index - 1], question_ans[B_index + offset:C_index - 1],
                                     question_ans[C_index + offset:], "No_D"])

                            self.question.append((question_ans[:A_index - 1]))
                        else:
                            A_index = question_ans.index("(1)")
                            B_index = question_ans.index("(2)")
                            C_index = question_ans.index("(3)")
                            if "(4)" in question_ans:
                                D_index = question_ans.index("(4)")
                                self.candidates.append(
                                    [question_ans[A_index + offset:B_index - 1], question_ans[B_index + offset:C_index - 1],
                                     question_ans[C_index + offset:D_index - 1], question_ans[D_index + offset:]])
                            else:
                                self.candidates.append(
                                    [question_ans[A_index + offset:B_index - 1], question_ans[B_index + offset:C_index - 1],
                                     question_ans[C_index + offset:], "No_D"])

                            self.question.append((question_ans[:A_index - 1]))

            return set(self.col_size), self.question,self.candidates, self.algebra_question

