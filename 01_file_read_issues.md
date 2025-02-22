### Problems
So there are some problems with our code

1. The invoke_main() method is a stupid naming convention. We need to have a sensible function name
2. We are reading all the lines of the file in a single go via readlines(). This will load up our memory. What if the file is in gigabytes?
3. We have not used any sort of "exception handling" if the file doesn't exist. 
4. We dont close the files we opened. Such things are very bad as they leave room for out of memory leaks
5. There is no object orientation concept used in the program. Everything is written in the invoke_main(). For this toy example, it all works fine as there are just 2/3 lines of code. But when you write a larger and complex logic, "segregation of duties" meaning what should each part of the program do becomes very important so you can manage the code well. 
6. The file name is hardcoded in the method that processes the file. Ideally it should come as a parameter from the main method.

We attempt to solve these issues in the next attempt: 01_file_read_prof.py