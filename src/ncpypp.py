#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@file
main program

@author: Sven Langer
@copyright: Sven Langer
'''

from ncpypp.parameter import Parameter
from ncpypp.pp import PP
import ncpypp.languages.iso.mitsubishi.mitsubishi
import ncpypp.languages.iso.mitsubishi.m700
from sys import argv
from os import chdir
from os.path import abspath, dirname


def get_help():
    '''
    @brief help text for usage
    @param None
    @return string-type helptext
    @exception None
    '''
    msg = "NcPyPP is a postprocessor engine for nc programs"
    return msg


def main(args):
    # for key, value in get_parameter(read_pyppfile()).items():
        # print(key, '\t', value)

    pp = PP('../input/example.i')
    # pp.parse()

if __name__ == "__main__":
    chdir(dirname(abspath(__file__)))
    main(argv[1:])
