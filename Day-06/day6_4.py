#coroutine continued
def running_total():
    total=0
    while True:
        number=yield total
        total += number
c= running_total()
print(next(c))
print(c.send(10))
print(c.send(20))
print(c.send(30))



#c = running_total()   # coroutine created, not started yet

#next(c)               # starts coroutine
#    total = 0
#    yield total → returns 0
#---------------------------------
#print(next(c)) → 0

#c.send(10)
#    number = 10
#    total = 0 + 10 = 10
#    yield total → returns 10
#---------------------------------
#print(c.send(10)) → 10

#c.send(20)
#    number = 20
#    total = 10 + 20 = 30
#   yield total → returns 30
#---------------------------------
#print(c.send(20)) → 30

#c.send(30)
#    number = 30
#    total = 30 + 30 = 60
#    yield total → returns 60
#---------------------------------
#print(c.send(30)) → 60


#CONTROL FLOW ==>
#[Caller] next(c) ──► [Coroutine] total=0 → yield 0
#        ◄────────── returns 0

#[Caller] c.send(10) ──► [Coroutine] number=10 → total=10 → yield 10
#        ◄───────────── returns 10

#[Caller] c.send(20) ──► [Coroutine] number=20 → total=30 → yield 30
#        ◄───────────── returns 30

#[Caller] c.send(30) ──► [Coroutine] number=30 → total=60 → yield 60
#        ◄───────────── returns 60
