#learning scope of variables along with nested functions
x = 10                             #global variable
 
def outer():                       #outer function 
    global x                  
    x = x + 10
    count=0
    def inner():                    #inner function 
        y = 100
        nonlocal count              #using nonlocal keyword
        count += 1
        print (f"count {count}")
        print (f"y {y}")
    inner()
    print (f"count {count}")
    print (f"x = {x}")
print(f"x = {x}")
outer()