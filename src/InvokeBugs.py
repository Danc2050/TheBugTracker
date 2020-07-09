# https://docs.python.org/3/library/exceptions.html#exception-hierarchy
# https://www.geeksforgeeks.org/built-exceptions-python/
# https://docs.python.org/2/library/exceptions.html

"""
Base Classes
"""


def invoke_exception():
    """
    All built-in, non-system-exiting exceptions are derived from this class. All user-defined exceptions
    should also be derived from this class.
    """
    raise Exception("This is a test exception")


def invoke_arithmeticError(i=0):
    """
    The base class for those built-in exceptions that are raised for various
    arithmetic errors: OverflowError, ZeroDivisionError, FloatingPointError.
    Change value of i to invoke a specific error
    """
    if i == 0:
        invoke_overflowError()
    if i == 1:
        invoke_zeroDivisionError()
    if i == 2:
        invoke_floatingPointError()


def invoke_bufferError():
    """
    Raised when a buffer related operation cannot be performed.
    """
    import io
    a = io.BytesIO(b'Hello')
    a.getbuffer()
    a.write(b' world!')


def invoke_lookupError(i=0):
    """
    The base class for the exceptions that are raised when a key or index used on
    a mapping or sequence is invalid: IndexError, KeyError. This can be raised directly by codecs.lookup().
    Change value of i to invoke a specific error
    """
    if i == 0:
        invoke_indexError()
    if i == 1:
        invoke_keyError()


"""
Concrete Exceptions
"""


def invoke_assertionError():
    """
    Raised when an assert statement fails.
    """
    a = 0
    assert a != 0
    return a


def invoke_attributeError():
    """
    Raised when an attribute reference (see Attribute references) or assignment fails.
    (When an object does not support attribute references or attribute assignments at all, TypeError is raised.)
    """
    a = 10
    a.append(6)
    return a


def invoke_EOFError():
    """
    Raised when the input() function hits an end-of-file condition (EOF) without reading any data.
    (N.B.: the io.IOBase.read() and io.IOBase.readline() methods return an empty string when they hit EOF.)
    """
    while True:
        data = input('You can produce an EOF error if you run this script in the terminal while program is running\n'
                     '$ echo hello | python InvokeBugs.py: ')
        print('You inputted:  ', data)


def invoke_floatingPointError():
    """
    A FloatingPointError is raised when a floating point operation fails.
    """
    import numpy
    with numpy.errstate(invalid='raise'):
        a = numpy.sqrt(-1)
    return a


def invoke_importError():
    """
    Raised when the import statement has troubles trying to load a module.
    Also raised when the “from list” in from ... import has a name that cannot be found.
    """
    from time import datetime


def invoke_moduleNotFoundError():
    """
    A subclass of ImportError which is raised by import when a module could not be located.
    It is also raised when None is found in sys.modules.
    """
    from exception import myexception


def invoke_indexError():
    """
    Raised when a sequence subscript is out of range.
    (Slice indices are silently truncated to fall in the allowed range;
    if an index is not an integer, TypeError is raised.)
    """
    a = [3, 7, 9]
    return a[3]


def invoke_keyError():
    """
    Raised when a mapping (dictionary) key is not found in the set of existing keys.
    """
    a = {'Jim': 30, 'Pam': 28}
    return a['Michael']


def invoke_keyboardInterrupt():
    """
    Raised when the user hits the interrupt key (normally Control-C or Delete).
    During execution, a check for interrupts is made regularly.
    """
    while True:
        input("You are in a forever loop: press ctrl-c to keyboard interrupt: ")


def invoke_memoryError():
    """
    Raised when an operation runs out of memory but the situation may still be rescued (by deleting some objects).
    """
    factors = []
    for i in range(1, 600851475143 + 1):
        if 600851475143 % i == 0:
            factors.append(i)
    print(factors)


def invoke_nameError():
    """
    Raised when a local or global name is not found. This applies only to unqualified names.
    The associated value is an error message that includes the name that could not be found.
    """
    return a


class notImplemented(object):
    """
    This is a class for the invoke_notImplmentedError function below
    """
    def notImplementedError(self):
        raise NotImplementedError()


def invoke_notImplementedError():
    """
    This exception is derived from RuntimeError.
    In user defined base classes, abstract methods should raise this exception when they require derived classes
    to override the method, or while the class is being developed to indicate that the real implementation still needs
    to be added.
    """
    s = notImplemented()
    return s.notImplementedError()


def invoke_OSError():
    """
    This exception is raised when a system function returns a system-related error,
    including I/O failures such as “file not found” or “disk full”
    (not for illegal argument types or other incidental errors).
    (only works on UNIX systems)
    """
    import os
    for i in range(5):
        print(i, os.ttyname(i))


def invoke_overflowError():
    """
    Raised when the result of an arithmetic operation is too large to be represented.
    For historical reasons, OverflowError is sometimes raised for integers that are outside a required range.
    """
    import math
    a = math.exp(1000)
    return a


def invoke_recursionError():
    """
    This exception is derived from RuntimeError. It is raised when the interpreter detects that the
    maximum recursion depth (see sys.getrecursionlimit()) is exceeded.
    """
    return invoke_recursionError()


def invoke_referenceError():
    """
    This exception is raised when a weak reference proxy, created by the weakref.proxy() function,
    is used to access an attribute of the referent after it has been garbage collected.
    """
    # PASS


def invoke_runtimeError():
    """
    Raised when an error is detected that doesn’t fall in any of the other categories.
    The associated value is a string indicating what precisely went wrong.
    """
    # PASS


def invoke_stopIteration():
    """
    Raised by built-in function next() and an iterator’s __next__() method to signal that
    there are no further items produced by the iterator.
    """
    a = [3, 1, 2]
    i = iter(a)
    print(i)
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
    return i


def invoke_stopAsyncIteration():
    """
    Must be raised by __anext__() method of an asynchronous iterator object to stop the iteration.
    """
    # PASS


def invoke_syntaxError():
    """
    Raised when the parser encounters a syntax error. This may occur in an import statement,
    in a call to the built-in functions exec() or eval(),
    or when reading the initial script or standard input (also interactively).
    """
    print(eval('This is a syntax error'))


def invoke_indentationError():
    """
    Base class for syntax errors related to incorrect indentation. This is a subclass of SyntaxError.
    """
    # PASS


def invoke_tabError():
    """
    Raised when indentation contains an inconsistent use of tabs and spaces. This is a subclass of IndentationError.
    """
    # PASS


def invoke_systemError():
    """
    Raised when the interpreter finds an internal error, but the situation does not look so
    serious to cause it to abandon all hope. The associated value is a string indicating what went wrong
    (in low-level terms).
    """
    # PASS


def invoke_systemExit():
    """
    This exception is raised by the sys.exit() function.
    It inherits from BaseException instead of Exception so that it is not accidentally
    caught by code that catches Exception.
    """
    # PASS


def invoke_typeError():
    """
    Raised when an operation or function is applied to an object of inappropriate type. The associated value is a string giving details about the type mismatch.
    """
    a = ('tuple',) + 'string'
    print(a)


def invoke_unboundLocalError():
    """
    Raised when a reference is made to a local variable in a function or method,
    but no value has been bound to that variable. This is a subclass of NameError.
    """
    local_val = local_val + 1
    print(local_val)


def invoke_unicodeError():
    """
    Raised when a Unicode-related encoding or decoding error occurs. It is a subclass of ValueError.
    """
    # PASS


def invoke_unicodeEncodeError():
    """
    Raised when a Unicode-related error occurs during encoding. It is a subclass of UnicodeError.
    """
    # PASS


def invoke_unicodeDecodeError():
    """
    Raised when a Unicode-related error occurs during decoding. It is a subclass of UnicodeError.
    """
    # PASS


def invoke_unicodeTranslateError():
    """
    Raised when a Unicode-related error occurs during translating. It is a subclass of UnicodeError.
    """
    # PASS


def invoke_valueError():
    """
    Raised when an operation or function receives an argument that has the right type but an inappropriate
    value, and the situation is not described by a more precise exception such as IndexError.
    """
    print(int('a'))


def invoke_zeroDivisionError():
    """
    Raised when the second argument of a division or modulo operation is zero.
    The associated value is a string indicating the type of the operands and the operation.
    """
    a = 7 / 0
    return a


def invoke_environmentError(i=0):
    """
    The base class for exceptions that can occur outside the Python system: IOError, OSError.
    Change value of i to invoke a specific error
    """
    if i == 0:
        invoke_IOError()
    if i == 1:
        invoke_OSError()


def invoke_IOError():
    """
    Raised when an I/O operation (such as a print statement,
    the built-in open() function or a method of a file object) fails for an I/O-related reason,
    e.g., “file not found” or “disk full”.
    """
    try:
        a = open("unexistant.txt", 'r')
    except IOError as e:
        print("IOError encountered")
        print(e)


def invoke_windowsError():
    """
    Raised when a Windows-specific error occurs or when the error number does not correspond to an errno value.
    (Only available on Windows systems)
    """
    try:
        a = open("unexistant.txt", 'r')
    except WindowsError as e:
        print("WindowsError encountered")
        print(e)


def invoke_blockingIOError():
    """
    Raised when an operation would block on an object (e.g. socket) set for non-blocking operation.
    """
    # PASS


def invoke_childProcessError():
    """
    Raised when an operation on a child process failed.
    """
    # PASS


def invoke_connectionError():
    """
    A base class for connection-related issues.
    Subclasses are BrokenPipeError, ConnectionAbortedError, ConnectionRefusedError and ConnectionResetError.
    """
    import requests
    from requests.exceptions import ConnectionError
    URL = "http://badAddress.com"
    location = "fakeLocation"
    try:
        r = requests.get(url=URL, params={'address': location})
    except ConnectionError as e:
        print("ConnectionError encountered")
        print(e)


def invoke_brokenPipeError():
    """
    A subclass of ConnectionError, raised when trying to write on a pipe while the other end has been closed,
    or trying to write on a socket which has been shutdown for writing.
    """
    # PASS


def invoke_connectionAbortedError():
    """
    A subclass of ConnectionError, raised when a connection attempt is aborted by the peer.
    """
    # PASS



def invoke_connectionRefusedError():
    """
    A subclass of ConnectionError, raised when a connection attempt is refused by the peer.
    """
    # PASS


def invoke_connectionResetError():
    """
    A subclass of ConnectionError, raised when a connection is reset by the peer.
    """
    # PASS



def invoke_fileExistsError():
    """
    Raised when trying to create a file or directory which already exists.
    """
    # PASS



def invoke_fileNotFoundError():
    """
    Raised when a file or directory is requested but doesn’t exist.
    """
    import os
    directory = "fake_file"
    parent_dir = "/fake/directory"
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)
    print("Directory '%s' created" % directory)


def invoke_InterruptedError():
    """
    Raised when a system call is interrupted by an incoming signal.
    """
    # PASS


def invoke_isADirectoryError():
    """
    Raised when a file operation (such as os.remove()) is requested on a directory.
    """
    # PASS


def invoke_notADirectoryError():
    """
    Raised when a directory operation (such as os.listdir()) is requested on something which is not a directory.
    """
    import os
    if not os.path.isdir("/fake/directory"):
        raise NotADirectoryError()


def invoke_permissionError():
    """
    Raised when trying to run an operation without the adequate access rights - for example filesystem permissions.
    """
    # PASS


def invoke_processLookupError():
    """
    Raised when a given process doesn’t exist.
    """
    # PASS


def invoke_timeoutError():
    """
    Raised when a system function timed out at the system level.
    """
    from requests.exceptions import Timeout
    import requests
    try:
        a = requests.get("https://httpstat.us/524", timeout=0.001)
    except Timeout as e:
        print("TimeoutError encountered")
        print(e)
        a = "No response"
