import os.path
import sys

def print_file_content(f):
    #This function reads from a file and prints its content 
    if f.mode == "r":
        content = f.read()
        print(content)
    else:
        print("File not found or not open.")

def print_file_line_by_line(f):
    #This methof will print the content of a file line by line
    for line in f:
        print(line)

def main():
    # This is the main body of the application
    
    # Check if file1 exists
    if os.path.exists("file1.txt"):
        # Opening 1st file for compare
        f1 = open("file1.txt", "r") # file to compare open for read only
        # Check if first file is open for read and print it's content if yes
        print_file_line_by_line(f1)
    else: 
        print("File1 not found.")
        sys.exit()

    # Check if file2 exists
    if os.path.exists("file2.txt"):
        # Opening 2nd file for compare
        f2 = open("file2.txt", "r") # file to compare open for read only
        # Check if first file is open for read and print it's content if yes
        print_file_line_by_line(f2)
    else: 
        print("File2 not found.")
        sys.exit()
    
    # Check if a results file already exists. 
    if os.path.exists("result_file.txt"):
        os.remove("result_file.txt")
        rezf = open("rezult_file.txt", "w+")
    else:
        rezf = open("rezult_file.txt", "w+")



if __name__ == "__main__":
    main()