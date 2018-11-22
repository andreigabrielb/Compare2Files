
def read_and_print():
    #This function reads from a file and prints its content 
    f = open("file1.txt", "r")
    if f.mode == "r":
        content = f.read()
        print(content)

if __name__ == "__main__":
    read_and_print()