#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@file
Mainprogram

@author: Sven Langer
@copyright: Sven Langer
'''

from parameter import GetParameter, ReadPyppfile, ValidateParameter
import Languages.Iso._Mitsubishi
import Languages.Iso.Mitsubishi._M700

import sys
import re

def GetHelp():
    '''
    Returns help file

    @author Sven Langer
    '''
    msg = "NcPyPP is a postprocessor engine for nc programs"
    return msg


def main(argv):
    # for key, value in ReadPyppfile('./Pyppfile').items():
    #    print(key,'\t', value)
    for key, value in GetParameter(ReadPyppfile()).items():
        print(key, '\t', value)
    ValidateParameter()

    if len(argv) > 0:
        if len(argv) > 1:
            print(GetHelp())
            return
        cmd = argv[0].lower()

        if cmd == "language":
            print(GetLanguage())
        elif cmd == "dialect":
            print(GetDialect())
        elif cmd == "machine":
            print(GetMachine())
        else:
            print(GetHelp())

if __name__ == "__main__":
    main(sys.argv[1:])
