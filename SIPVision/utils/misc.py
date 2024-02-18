"""
MISC

"""
import argparse
import ast
import re 

def natural_key(string_):
    """See http://www.codinghorror.com/blog/archives/001018.html"""
    """Natural sorting is particularly useful when you have strings that include numbers, and you want them sorted in a way that is intuitive to humans."""
    return [int(s) if s.isdigit() else s for s in re.split(r'(\d+)', string_.lower())]