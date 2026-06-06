import pickle

# Reading records from the binary file
with open("Day-07/data3.dat","rb") as f:
    while True:
        try:
            record=pickle.load(f)

            print("Integer: ",record["integer"])
            print("Float: ",record["float"])
            print("String: ",record["string"])
            print("List: ",record["list"])

            print("-"*50)

        except EOFError:
            # EOFError occurs when end of file is reached
            break