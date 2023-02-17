"""
Authors: Aydan O'Brien and Nicholas Engle


param s: string to check
return: True if string is a palindrome, False otherwise
"""

def palindrome(s: str) -> bool:
    return s == s[::-1]