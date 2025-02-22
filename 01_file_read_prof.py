# The goal of the program is to
# 1. Read a local file
# 2. Read all the contents of a file into a list
# 3. Print the list

# So instead of reading the entire file in memory we are going to "read it parts" and print it in parts. What that means
# is we read it specific chunks and print those chunks. A similar approach is used by Netflix when it streams movie on
# your device so the concept is not new. Thus, we need to define the chunk size by defining a constant like so...

CHUNK_SIZE = 1024 * 8  # 1024 bytes x 8 = 8kb. This is our chunk size which means we will read 8kb of data each time from the file.


# We now name a sensible method called print_file which will take in a reference of the file and attempt to read and print it.
def print_file(file_name):
    """
    using the system call open(), we open the file and read all the contents into a list and print it on the console
    :param file_name to be read
    :return: none
    """

    # We will now "try-catch" our operation of reading the file. If the file doesn't exist or if there is any error while
    # reading the file, the except: block will be invoked and a user-friendly message will be printed.
    try:

        # we will use the construct "with" provided by the python runtime. This ensures that the file handles are closed at
        # the OS level, and we don't have to specifically code for it. Functionally it is the same as before except this time
        # the with construct assigns the file's handle to the variable "f" and you can invoke the file reading operations
        # using "f". For example - you could write: lines = f.readlines() just like before.
        with open(file_name, "r") as f:

            # the next is a simple "endless while loop" which means it will repeat forever unless you explicitly break it.
            # The idea here is we "keep on reading" the file until there is no data left and at that point, we break this
            # infinite loop. That is shown on line# 36, 37
            while True:
                # we start reading the data in chunks. We have already defined the chunk size as 8KB on line# 10
                data_chunk = f.read(CHUNK_SIZE) # remember - f was given to us by the "with construct" on line# 29

                # we check to see if the data_chunk is actually valid i.e. the data is indeed being returned by the OS.
                # if not, then we will get a "NULL" and that's when we break the loop. The following if condition takes
                # care of that.
                if not data_chunk:
                    break

                # if the above "if condition" fails, that means that the data chunk is valid, we print it.
                print(data_chunk)

                # If you run this program, you will see the file contents getting printed, but how can you ascertain that
                # we are indeed reading in chunks? For that, here is a small tweaking to do -
                # 1. Change the chunk_size above to 512 bytes i.e. CHUNK_SIZE = 512 and
                # 2. Enable the line below. Once you do that, you will see ---- getting printed after every 512 bytes
                # print ("----")
    except (IOError, OSError) as e:
        # in the exception block, when there is an error, we are saying we are interested to catch any IO Error or any
        # OS level error and if any of those cases happen, please wrap the exception in the variable "e" and give it to us

        print("Error reading file: {}".format(file_name))
        # Here we are not really "handling the exception" we are merely printing it as shown below. But we do print a
        # "contextual" information that "Error was encountered reading the file..." and we print the file name in the
        # statement above. What we are doing here is concatenating the string message with name of the file that was
        # passed to us as an argument of the function. This way of appending the filename to a string is called "parameter
        # substitution". The parameter being the "file_name" which is being substituted in the place of "{}" in the string
        print(e)

        # Note that "format" is a function provided by string data type in python. So you can write
        # println ("I am {}, and my age is {}".format("Abhay", 45)) and it will print - I am Abhay and, my age is 45.


if __name__ == '__main__':
    print_file("quotes.txt")

# as before you can see that the execution of the program begins from the main i.e. line# 68, and it will invoke the
# print_file by passing in the actual file name.