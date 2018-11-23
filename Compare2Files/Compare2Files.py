import os.path
import sys

def count_file_lines(fname):
    #This function will return the number of lines in a file
    f = open(fname, "r")
    i = 0;
    for line in f:
        i = i + 1
    f.close()
    return i

def print_file_content(fname):
    #This method reads from a file and prints its content 
    f = open(fname, "r")
    print(f.read())
    print
    f.close()

def check_file_existance(fname):
    #This functionl will check if a file exists or show error if not

    if os.path.exists(fname):
        # Check if file exists and if yes will print its content
        print_file_content(fname)
    else: 
        print(fname + " not found.")
        sys.exit()


def main():
    # This is the main body of the application
    
    # Create variables with the file names
    fname1 = "file1.txt"
    fname2 = "file2.txt"
    rezfname = "rezult_file.txt"

    # Check if files exist and display their content
    check_file_existance(fname1)
    check_file_existance(fname2)

    # Create clean results file
    rezf = open(rezfname, "w+")
    rezf.close()

    # Count the number of lines in the files and display them
    nl_f1 = count_file_lines(fname1)
    nl_f2 = count_file_lines(fname2)

    print("The 1st file has %d lines." % nl_f1)
    print("The 2nd file has %d lines." % nl_f2)
    print(count_file_lines(rezfname))
    

"""
    # Check if file2 exists
    if os.path.exists("file2.txt"):
        # Opening 2nd file for compare
        f2 = open("file2.txt", "r") # file to compare open for read only
        # Check if first file is open for read and print it's content if yes
        nl_f2 = count_file_lines(f2)
    else: 
        print("File2 not found.")
        sys.exit()
    
    # Check if a results file already exists. 
    if os.path.exists("result_file.txt"):
        os.remove("result_file.txt")
        rezf = open("rezult_file.txt", "w+")
    else:
        rezf = open("rezult_file.txt", "w+")
 
    print("The 1st file has: ", nl_f1)
    print("The 2nd file has: ", nl_f2)
    print(print_file_line_by_line(rezf))

    #Close all of the open files here
    f1.close()
    f2.close()
"""

if __name__ == "__main__":
    main()