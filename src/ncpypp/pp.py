#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@file
<brief description>

@author: Sven Langer
@copyright: Sven Langer
'''

import re
from ncpypp.parameter import Parameter
from ncpypp.languages.pypplang import Pypplang


class PP:

    def __init__(self, file):
        self.p = Parameter()
        self.o = self.p.in_mod.Instance()
        self.t = Pypplang()

        self.input = file
        self.output = self.input + '.out'
        self.temp = self.input + '.tmp'
        self.parse()

    def parse(self):
        with open(self.temp, 'w') as temp:
            with open(self.output, 'w') as output:
                with open(self.input, 'r') as input:
                    l = ''
                    for line in input:
                        l += line.strip()
                        if l.startswith("[[") and not l.endswith("]]"):
                            continue
                        # remove numbers
                        s = self.o.remove_numbers(l)
                        # expand macro
                        s = self.t.expand(s)
                        temp.write(s)
                        s = self.o.expand(s)
                        output.write(s)
                        l = ''

    def expand(self, str):
        if str.lower() == 'lorem':
            return self.lorem()

