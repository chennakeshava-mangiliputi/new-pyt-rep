class Marks:
    def __init__(self):
        self.__mathmarks=0
    def getMathmarks(self):
        return self.__mathmarks
    def setMathmarks(self,marks):
        self.__mathmarks=marks
s1=Marks()
print(s1.getMathmarks())
s1.setMathmarks(50)
print(s1.getMathmarks())