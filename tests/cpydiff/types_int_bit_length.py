"""
categories: Types,int
description: ``bit_length`` method doesn't exist.
cause: bit_length method is not implemented.
workaround: Avoid using this method on MicroPython.
"""


x = 255
print(f"{x} is {x.bit_length()} bits long.")
