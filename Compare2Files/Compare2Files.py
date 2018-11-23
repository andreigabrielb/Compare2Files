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
    #This functionl will check if a file exists and has data or show error if not

    # Check if file exists
    if os.path.exists(fname):
        #check if files are empty 
        if os.path.getsize(fname) > 0:
            print_file_content(fname)
        #close the app file is empty
        else:
            print(fname + " is empty!")
            sys.exit()
    #close the application is file is not available
    else: 
        print(fname + " not found!")
        sys.exit()

def return_lines_from_file(fname):
    # This function is meant to return a line [ln] from a file [fname]
    f = open(fname, "r")
    fl = f.readlines()
    f.close()
    return fl

def main():
    # This is the main body of the application
    
    # Create variables with the file names
    fname1 = "file1.txt"
    fname2 = "file2.txt"
    rezfname = "rezult_file.txt"

    # Check if files exist, have data and display their content
    check_file_existance(fname1)
    check_file_existance(fname2)

    # Count the number of lines in the files and display them
    nl_f1 = count_file_lines(fname1)
    nl_f2 = count_file_lines(fname2)
    print("The 1st file has %d lines." % nl_f1)
    print("The 2nd file has %d lines." % nl_f2)

    # Get linies from lines from file as a list of strings
    fl1 = return_lines_from_file(fname1)
    fl2 = return_lines_from_file(fname2)

    # Create clean results file
    rezf = open(rezfname, "w+")

    # Determine if the files have the same number of lines 
    if nl_f1 <> nl_f2:
        max_ln = max(nl_f1, nl_f2)

    

    rezf.close()

    check_file_existance(rezfname)

if __name__ == "__main__":
    main()