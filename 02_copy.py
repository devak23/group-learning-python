# the goal of this program is to make a copy of an existing file


# So we define a function that takes 2 parameters - a source file and the name by which you want to create the new file
def copy_manually(orig_file, copy_file):
    """
    Accepts original file and the new name of the file and creates a copy of the original file
    :param orig_file - the file whose copy is to be made
    :param copy_file - the file which should be the copy
    :return none
    """

    with open(orig_file, "r") as source:
        # we now open the second file handle in "append mode" and use that handle as "dest"
        with open(copy_file, "+a") as dest:
            # again, we read all the lines and write them in the new file
            dest.writelines(source.readlines())


# We always try to utilize what is out there instead of reinventing the wheel. Shutil is a module in the python core
# library that is available to us directly, so we can readily use it like this.

import shutil # the module in python's system that allows us to use their API

def copy_via_util(orig_file, copy_file):
    """
    Copies the file via python's builtin module shutil (shell utils)
    :param orig_file - the file whose copy is to be made
    :param copy_file - the file which should be the copy
    :return none
    """

    shutil.copy(orig_file, copy_file)


if __name__ == "__main__":
    #copy_manually("quotes.txt", "quotes-copy-manual.txt")
    copy_via_util("quotes.txt", "quotes-copy-util.txt")
