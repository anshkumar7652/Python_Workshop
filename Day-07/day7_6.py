import pickle

# Creating a binary file and storing records using pickle
with open("Day-07/data3.dat", "wb") as f:
    while True:
        num=int(input("enter an integer: "))
        price=float(input("enter a float: "))
        name=input("enter a string: ")
        lst=input("enter list elements separated by space: ").split()

        # store all values in a dictionary
        record={
            "integer":num,
            "float":price,
            "string":name,
            "list":lst
        }

        # write record to binary file
        pickle.dump(record,f)

        choice=input("DO YOU WANT TO ADD MORE RECORDS? (y/n): ")

        if(choice.lower()!='y'):
            break

print("data saved successfully")