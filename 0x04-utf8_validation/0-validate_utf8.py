#!/usr/bin/python3
"""UTF-8 Validation"""


def get_set_bits(number):
    """get set bits"""
    set_the_bits = 0
    helper = 1 << 7
    while helper & number:
        set_the_bits += 1
        helper = helper >> 1
    return set_the_bits


def validUTF8(data):
    """a method that determines if a given data 
        set represents a valid UTF-8 encoding.
    """
    bits_count = 0
    for i in range(len(data)):
        if bits_count == 0:
            bits_count = get_set_bits(data[i])
            '''1-byte (format: 0xxxxxxx)'''
            if bits_count == 0:
                continue
            '''a character in UTF-8 can be 1 to 4 bytes long'''
            if bits_count == 1 or bits_count > 4:
                return False
        else:
            '''checks if current byte has format 10xxxxxx'''
            if not (data[i] & (1 << 7) and not (data[i] & (1 << 6))):
                return False
        bits_count -= 1
    return bits_count == 0
