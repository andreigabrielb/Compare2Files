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
    print(fname + "--------------------------------\n" )
    f = open(fname, "r")
    print(f.read())
    print("-----------------------------\n")
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

def string_differences(str1, str2):
    # This fucntion will return the number of different chararters between string 1 and string 2 and the differences character index location
    diff_count = 0
    diff_str = ""

    if str1 == "\n":
        diff_count = len(str2)
        diff_str = " This line is empty in the 1st file."
        string_result = str(diff_count) + diff_str
        return string_result

    elif str2 == "\n":
        diff_count = len(str1)
        diff_str ="This line is empty in the 2nd file."
        string_result = str(diff_count) + diff_str
        return string_result

    else:
        row_lenght = min(len(str1), len(str2))

        for i in range(row_lenght-1):
            if str1[i] <> str2[i]:
                diff_count += 1
                diff_str += str(i+1)
            else:
                diff_str += " "

        if len(str1) > len(str2):
            diff_count += (len(str1) - len(str2))
            for i in range(len(str2)-1, len(str1)-1, 1):
                diff_str += str(i+1)

        elif len(str1) < len(str2):
            diff_count += (len(str2) - len(str1))
            for i in range(len(str2)-1, len(str1)-1, 1):
                diff_str += str(i+1)

    #print(diff_count)
    #print(diff_str)
    string_result = str(diff_count) + diff_str
    return string_result

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

    # Get linies from lines from file as a list of strings
    fl1 = return_lines_from_file(fname1)
    fl2 = return_lines_from_file(fname2)

    # Create clean results file
    rezf = open(rezfname, "w+")

    # Determine if the files have the same number of lines 
    if nl_f1 <> nl_f2:
        min_ln = min(nl_f1, nl_f2)

    # Go through each of the file lines and compare them
    for i in range(min_ln-1):
        if fl1[i] == fl2[i]:
            rezf.write("[Line %d Differences = 0] \n" % (i+1))
        else:
            result_string = rezf.write(string_differences(fl1[i], fl2[i]))
            rezf.write("[Line %d Differences = %s\n]" % ((i+1), result_string))
            

    # In case one file has more lines than the other write in the results which one has more lines
    if nl_f1 > nl_f2:
        rezf.write("%s has %d more lines than %s \n" % (fname1, nl_f1 - nl_f2, fname2))
    elif nl_f1 < nl_f2:
        rezf.write("%s has %d more lines than %s \n" % (fname1, nl_f1 - nl_f2, fname2))
    #Close results file
    rezf.close()

    print_file_content(rezfname)


if __name__ == "__main__":
    main()