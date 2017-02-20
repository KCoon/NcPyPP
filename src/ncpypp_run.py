#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@file
main program

@author: Sven Langer
@copyright: Sven Langer
'''

from sys import argv
from os import chdir
from os.path import abspath, dirname
from ncpypp.pp import PP


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
    '''
    @brief entry point of the application
    @param <string-type> commandline arguments
    @return None
    @exception None
    '''

    # for key, value in get_parameter(read_pyppfile()).items():
    # print(key, '\t', value)

    print(args)
    parser = PP('../input/example.i')
    parser.parse()


if __name__ == "__main__":
    chdir(dirname(abspath(__file__)))
    main(argv[1:])
