import SeqManager
FibSeq=SeqManager.Sequence([1,1])
# This file proves task 4

class Task4:
    def __init__(self,lengthTest) -> None:
        self.FibSeq=SeqManager.Sequence([1,1])
        self.lengthTest=lengthTest

    def calculateDif(self,val):
        return val[0]*val[2]-val[1]*val[1]
    
    def getSection(self):
        FibSeq.generateSeq(self.lengthTest)
        self.sequence=FibSeq.sequence
        r=0
        while r != len(self.sequence)-2:
            val=[self.sequence[r],self.sequence[r+1],self.sequence[r+2]]
#            return val[0]*val[2]-val[1]*val[1]
            print('Trial: '+str(r+1))
            print('Surrounding Numbers: '+str(val[0])+', '+str(val[2])+': '+str(val[0]*val[2]))
            print('Middle Number: '+str(val[1])+': '+str(val[1]*val[1]))
            print('')
            print('Difference: '+str(val[0]*val[2]-val[1]*val[1]))
            print('')
            r=r+1



Task4Calc=Task4(50)
Task4Calc.getSection()