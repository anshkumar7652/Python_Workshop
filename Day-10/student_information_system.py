class Student:
    def info(self,n,erp):
        self.n=n
        self.erp=erp
    def display(self):
        print(self.n,"\n",self.erp)
obj=Student()
n=input('enter name of the student: ')
erp=int(input('Enter erp of the student: '))
obj.info(n,erp)
obj.display()