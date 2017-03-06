#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@file
<brief description>

@author: Sven Langer
@copyright: Sven Langer
'''

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

    def parse(self):
        with open(self.temp, 'w') as temp:
            with open(self.output, 'w') as output:
                with open(self.input, 'r') as input:
                    l = ''
                    output.write(self.o.id_ + '\n')
                    for line in input:
                        l += line.strip()
                        if l.startswith("[[") and not l.endswith("]]"):
                            continue
                        # remove numbers
                        s = self.o.remove_numbers(l)
                        # expand macro
                        s = self.t.expand(s)
                        temp.write(s)
                        for line2 in s.splitlines():
                            output.write(self.o.expand(line2))
                        l = ''

    def expand(self, str):
        if str.lower() == 'lorem':
            return self.o.lorem()