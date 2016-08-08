#!/usr/bin/env python
# HW04_ch08_ex04

# The following functions are all intended to check whether a string contains
# any lowercase letters, but at least some of them are wrong. For each
# function, describe (is the docstring) what the function actually does.
# You can assume that the parameter is a string.

# Do not merely paste the output as a counterexample into the documentation
# string, explain what is wrong.

###############################################################################
# Body


def any_lowercase1(s):
    """Explain what is wrong, if anything, here.
    the function stops after checking the first letter """
    for c in s:
        if c.islower():
            return True
        else:
            return False

def any_lowercase2(s):
    """Explain what is wrong, if anything, here.
    'c' will always return as true - should not have '' """
    for c in s:
        if 'c'.islower(): 
            return 'True' 
        else:
            return 'False'

def any_lowercase3(s):
    """Explain what is wrong, if anything, here.
    this function only returns whether or not the last letter is lower case, not whether there are lower case letters in the string. """
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s):
    """Explain what is wrong, if anything, here.
    flag is called out first (which is false) and says that lower case letters aren't lower case """
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


def any_lowercase5(s):
    """Explain what is wrong, if anything, here.
    If the first letter of the string is capitalized, it won't check the rest of the string for lower case letters and it will give you a False statement """
    for c in s:
        if not c.islower():
            return False
    return True


###############################################################################
def main():

    # Remove print("Hello World!") and for each function above that is wrong,
    # call that function with a string for which the function returns
    # incorrectly.
any_lowercase_("thisstringmessesupthefunction")
   


if __name__ == '__main__':
    main()
