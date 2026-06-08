#learing basic oops concepts
class Stud:
    def inputval(self):
            self.name=input('Enter student name: ')              #instance variable
            self.rn=int(input('Enter roll no.: '))
            self.fee=float(input('Enter fee: '))
            

    def printval(self):
          print(self.rn,self.name,self.fee,sep='-')
    
#main
s1=Stud()                            #constructor  call for object s1
s2=Stud()                            #constructor  call for object s2
s1.inputval()
s2.inputval()
s1.printval()
s2.printval()