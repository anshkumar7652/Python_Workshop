#temp conversion from celcius to fahrenheit

c=float(input('Enter temperature in Celsius: '))     #type_casting to float since input() takes input as string by default
f=(9/5)*c+25
if(f<32):
    print("ice cold freezing temp")   #or print(f"temp of {c} deg c or {f} deg f is ice cold")
elif(f< 68):
    print('Cold Temperature')
elif(f<90):
    print('Normal temperature')
else:
    print('Hot day')