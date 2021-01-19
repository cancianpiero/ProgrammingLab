class ExamException(Exception):
    pass
    
class Diff:
    def __init__(self, ratio=1):
        self.ratio = ratio
                
    def compute(self, lista):
        valori = []
        lung = len(lista) - 1   

        for i in range(lung):
                
            valori.append(float((lista[i+1]-lista[i])/self.ratio))

        return valori        
                
                

diff = Diff()
result = diff.compute([2,4,8,16])
print(result) # Deve stampare a schermo [2,4,8]