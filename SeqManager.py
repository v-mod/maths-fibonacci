class Sequence:
    def __init__(self,sequence) -> None:
        self.sequence=sequence
    
    def add(self,add): return self.sequence.append(add)
    def get(self,point): return self.sequence[point]
    def getLast2(self): return [self.sequence[len(self.sequence)-1],self.sequence[len(self.sequence)-2]]
    def generateNextSeq(self): return self.getLast2()[0]+self.getLast2()[1]
    def generateSeq(self,length):
        while length != 0:
            self.add(self.generateNextSeq())
            length=length-1
        return self.sequence