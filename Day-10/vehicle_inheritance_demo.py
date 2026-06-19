class car:
    def c_info(self,c_name):
        self.c_name=c_name
        print(self.c_name)
class vehicle(car):
    def bike(self,b_name):
        self.b_name=b_name
        print(self.b_name)

#main
obj=vehicle()
b_name=input('enter name of bike: ')
c_name=input('enter name of car: ')
obj.bike(b_name)
obj.c_info(c_name)