# The goal of the program is to
# 1. Read a local file
# 2. Read all the contents of a file into a list
# 3. Print the list

def invoke_main():
    """
    using the system call open(), we open the file and read all the contents into a list and print it on the console
    :return: none
    """
    lines = open("quotes.txt", "r").readlines()
    for line in lines:
        print (line)


if __name__ == '__main__':
    invoke_main()