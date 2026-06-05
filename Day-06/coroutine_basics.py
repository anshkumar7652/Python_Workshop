#coroutine and yield
#multiple resumes at yield

def coroutine():      #special function in python that can pause  and resume execution
    print('Coroutine started')

    while True:
        x=yield
        print('Received:',x)
        
c=coroutine()         #creates couroutine object but does not runs it yet
#next(c)              #start the coroutine
c.send(None)          #start the coroutine, runs until first yield (suspends or pauses at first yield found)
c.send(10)            #assigns 10 and resumes from where its paused and prints 'received 10'
c.send(20)            #assigns 20 and resumes again from where it was paused at first and prints 'received 20'
c.send(30)            #same for this




#Coroutine created (not running yet)
#        |
#c.send(None) → "Coroutine started"
#        |
#  yield suspends, waiting for input
#        |
#c.send(10) → resumes → x=10 → "Received: 10"
#        |
#   yield suspends again
#        |
#c.send(20) → resumes → x=20 → "Received: 20"
#        |
#   yield suspends again
#        |
#c.send(30) → resumes → x=30 → "Received: 30"
