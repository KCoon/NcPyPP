''' todo doc-string '''
import re
from os import listdir
from os.path import isfile, join, isdir
import importlib


class Parameter:

    def __init__(self, Pyppfile=None):
        # default parameter
        self.parameter = {'PATH_LANGUAGE': './ncpypp/languages',
                          'INPUT_LANGUAGE': None,
                          'INPUT_DIALECT': None,
                          'INPUT_INSTANCE': None,
                          'OUTPUT_LANGUAGE': None,
                          'OUTPUT_DIALECT': None,
                          'OUTPUT_INSTANCE': None,
                          'NUMBER': 'YES',
                          'USE_SUBROUTINES': 'NO'}

        # read Pyppfile
        if Pyppfile is None:
            Pyppfile = './Pyppfile'
        self.read_pyppfile(Pyppfile)

        # get available instances, dialects and languages
        # by parsing directory tree
        self.instances, self.dialects, self.languages = self._get_instances()
        self._load_modules()

    def read_pyppfile(self, path):
        para = {}
        print(path)
        import os
        print(os.getcwd())
        with open(path, 'r') as f:
            for line in f:
                line = line.strip()
                if line.startswith('#') or line == "":
                    continue
                m = re.search(r'''^([A-Z_-]*)\s*={1}\s*([\./\w\d-]*)$''', line)
                if m is not None:
                    self.parameter[m.group(1)] = m.group(2)
                else:
                    raise Exception('syntax error', line)
        return para

    # todo
    def validate_parameter(self):
        # PATH_LANGUAGE
        if not isdir(self.parameter['PATH_LANGUAGE']):
            raise Exception('PATH_LANGUAGE directory does not exist.')
        # INPUT_LANGUAGE
        if self.parameter['INPUT_LANGUAGE'] not in self.languages:
            raise Exception('INPUT_LANGUAGE', self.parameter[
                'INPUT_LANGUAGE'], 'unknown')
        # INPUT_DIALECT
        if self.parameter['INPUT_LANGUAGE'] + '/' + \
           self.parameter['INPUT_DIALECT'] not in self.dialects:
            raise Exception('INPUT_DIALECT', self.parameter[
                'INPUT_DIALECT'], 'unknown')
        # INPUT_MACHINE
        if self.parameter['INPUT_LANGUAGE'] + '/' + \
           self.parameter['INPUT_DIALECT'] + '/' + \
           self.parameter['INPUT_INSTANCE'] not in self.instances:
            raise Exception('INPUT_INSTANCE', self.parameter[
                'INPUT_INSTANCE'], 'unknown')
        # OUTPUT_LANGUAGE
        if self.parameter['OUTPUT_LANGUAGE'] not in self.languages:
            raise Exception('OUTPUT_LANGUAGE', self.parameter[
                'OUTPUT_LANGUAGE'], 'unknown')
        # OUTPUT_DIALECT
        if self.parameter['OUTPUT_LANGUAGE'] + '/' + \
           self.parameter['OUTPUT_DIALECT'] not in self.dialects:
            raise Exception('OUTPUT_DIALECT', self.parameter[
                'OUTPUT_DIALECT'], 'unknown')
        # OUTPUT_MACHINE
        if self.parameter['OUTPUT_LANGUAGE'] + '/' + \
           self.parameter['OUTPUT_DIALECT'] + '/' + \
           self.parameter['OUTPUT_INSTANCE'] not in self.instances:
            raise Exception('OUTPUT_INSTANCE', self.parameter[
                'OUTPUT_INSTANCE'], 'unknown')

    def _get_languages(self):
        """
        Returns installed languages.
        """
        langs = []
        for f in listdir(self.parameter['PATH_LANGUAGE']):
            if isdir(join(self.parameter['PATH_LANGUAGE'], f)) and \
                    re.search("^__.*__$", f) is None:
                langs.append(f)
        return langs

    def _get_dialects(self):
        """
        Returns installed dialects.
        """
        langs = self._get_languages()
        dials = []
        for lang in langs:
            dirs = join(self.parameter['PATH_LANGUAGE'], lang)
            for f in listdir(dirs):
                if isdir(join(dirs, f)) and re.search("^__.*__$", f) is None:
                    dials.append(lang + '/' + f)
        return dials, langs

    def _get_instances(self):
        """
        Returns installed languages.
        """
        dials, langs = self._get_dialects()
        instances = []
        for dial in dials:
            dirs = self.parameter['PATH_LANGUAGE'] + '/' + dial
            for f in listdir(dirs):
                if isfile(join(dirs, f)) and \
                   re.search(r"^[a-z]\w*.py$", f) is not None:
                    instances.append(dial + '/' + f[:-3])
        return instances, dials, langs

    def _load_modules(self):
        if self.parameter['INPUT_INSTANCE'] is not "":
            self.in_mod = importlib.import_module(
                'ncpypp.languages' + '.' +
                self.parameter['INPUT_LANGUAGE'] + '.' +
                self.parameter['INPUT_DIALECT'] + '.' +
                self.parameter['INPUT_INSTANCE'])
        elif self.parameter['INPUT_DIALECT'] is not "":
            self.in_mod = importlib.import_module(
                'ncpypp.languages' + '.' +
                self.parameter['INPUT_LANGUAGE'] + '.' +
                self.parameter['INPUT_DIALECT'] + '.' +
                self.parameter['INPUT_DIALECT'])
        else:
            self.in_mod = importlib.import_module(
                'ncpypp.languages' + '.' +
                self.parameter['INPUT_LANGUAGE'] + '.' +
                self.parameter['INPUT_LANGUAGE'])
