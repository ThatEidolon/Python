from ctypes import *

msvcrt = cdll.msvcrt
message_string = "Hello World!"
msvcrt.printf("Testing: %s", message_string)
