import os.path

def print_file_content(f):
    #This function reads from a file and prints its content 
    if f.mode == "r":
        content = f.read()
        print(content)
    else:
        print("File not found or not open.")

def main():
    # This is the main body of the application

    # Opening first file for compare
    f1 = open("file1.txt", "r") # file to compare open for read only

    # Check if first file is open for read and print it's content if yes
    print_file_content(f1)

    f2 = open("file2.txt", "r") # file to compare open for read only

     # Check if first file is open for read and print it's content if yes
    print_file_content(f2)
    
    # Check if a results file already exists. 
    if os.path.exists("result_file.txt"):
        os.remove("result_file.txt")
        rezf = open("rezult_file.txt", "w+")
    else:
        rezf = open("rezult_file.txt", "w+")

if __name__ == "__main__":
    main()