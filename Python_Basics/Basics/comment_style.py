## doc string
def greet(word):
    """
    Print a word with an
    exclamation mark following it.
    """
    print(word + "!")

greet("Hello World")


##Access Doc Strings

def greet(word):
    """
    Print a word with an
    exclamation mark following it.
    """
    print(word + "!")

# What the fucntion does?
print(greet.__doc__)

# Make sense, now lets use it    
greet("Hello World")


##doc string with styling guide
def square_root(n):
    """Calculate the square root of a number.

    Args:
        n: the number to get the square root of.
    Returns:
        the square root of n.
    Raises:
        TypeError: if n is not a number.
        ValueError: if n is negative.

    """
    pass