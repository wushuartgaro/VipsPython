# -*- coding: utf-8 -*-
"""
@author: CJR
"""

'''
main function
'''
import Vips
from urllib.parse import unquote

def main():
    vips = Vips.Vips(unquote("http://adam.goucher.ca/parkcalc/", encoding="utf-8"))
    vips.setRound(2)
    vips.service()
    
main()
