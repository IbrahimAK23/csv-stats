class stats:
    def __init__(self,numbers):
        self.numbers=numbers

    def count(self):
        
         
        
        return len(self.numbers)

    def mean(self):
        if len(self.numbers)==0:
            return None

        return sum(self.numbers)/len(self.numbers)

    def max(self):
        if len(self.numbers)==0:
            return None
        return max(self.numbers)

    def min(self):
        if len(self.numbers)==0:
            return None

        return min(self.numbers)


if __name__ == "__main__":

 numb=stats([0,1,2])

 print(numb.min())
 print(numb.mean())
 print(numb.max())
 print(numb.count())

 print(stats([]).mean())
