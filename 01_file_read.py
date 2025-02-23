# The goal of the program is to
# 1. Read a local file
# 2. Read all the contents of a file into a list
# 3. Print the list

# When you want to define a function in python, you should use the def keyword. You can see that this function (not
# named properly)
def invoke_main():
    """
    using the system call open(), we open the file and read all the contents into a list and print it on the console
    :return: none
    """

    # The above lines are called docstring comments these are used to generate documentation for your program. They can
    # have multiple params (depending on how your function is defined) or none as in this case. The :return: signifies
    # this program has nothing to return to its caller. Usually writing docstrings is a good practise. You should do it.
    # Please note the tripple quotes - its a multi line comment so that you can write the whole comment as a paragraph.

    lines = open("quotes.txt", "r").readlines()
    # In the above line we did several things. We made a call to open() function which is a part of the python's core
    # library that asks the operating system to open the file quotes.txt in "r" (readonly) mode. That call resulted
    # in the OS to return a "handle" to the file (present on the disk) to the "python's system". Python then wrapped
    # the file handle into its own implementation of the "file object" for us to use. We then invoked readlines() method
    # on python's file object which in turn invokes the readlines() on the file handle, which invokes another OS call to
    # which reads the file. This readlines method is provided by the "file object" exposed in python and returns the
    # data from the file - line by line into a "list". Each entry in the list is one line from the file. We then
    # assign this list to a local variable called "lines" which is then ready to be printed. Notice there is no need to
    # specify anything before "lines variable" to declare it as a "list type" of object. In Java and many other languages
    # the compiler requires us to define the "type" of the handle. Lucky for us, python is very developer friendly.


    for line in lines:
        print (line)
    # The above is a simple for loop which says: for each "line" (local variable created by us within the for loop) in
    # lines (variable defined by us on line# 20 (the list returned from reading the file), we are going to print the
    # contents of the variable --> line.


if __name__ == '__main__':
    invoke_main()
# the execution of the python program begins with the main method. So when the python interpreter tries to execute the
# code it will look for it within this file and will start executing line by line. But since we have defined our function
# invoke_method() first, it wont execute it but rather just "parse it" and keep it ready for execution. When it encounters
# the line #39 above, it will identify that step as the starting point and start running the program from this point on.
# What that if statement means is a bit complicated, and you can ignore it for now, but all it means is that the python
# interpreter will start from line# 40 and will look for the function invoke_main() to run the program. You should try
# running the program and see that it prints the file as expected.


# Please go to 01_file_read_issues.md for discussion of problems with this code.