#using decorator

def decorato(fun):
    def wrappe():
        print('Before function call')
        fun()
        print('After function call')
    return wrappe
@decorato              # python automatically does: greet =decorato(greet)
def greet():
    print('Hello!')
#greet= decorato(greet)
greet()
'''decorato() recieves greet() ,wraps it with additional behaviour,and returns the new function'''