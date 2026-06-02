#Write a program to convert an Upper case character into lower case and vice-versa
ch=input('enter a charcter: ')

if(ch.islower()):
    ch=ch.upper()
    print(f'case changed from {ch.lower()} to {ch}')
elif(ch.isupper()):
    ch=ch.lower()
    print(f'case changed from {ch.upper()} to {ch}')
else:
    print("Invalid input")