import re
from os import listdir
import os.path
from os.path import isfile, join, isdir

def ReadPyppfile(path='./Pyppfile'):
    para = {}
    with open(path, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('#') or line == "":
                continue
            m = re.search(r'''^([A-Z_-]*)\s*={1}\s*([\./\w\d-]*)$''',line)
            if m is not None:
                para[m.group(1)] = m.group(2)
            else:
                raise Exception('syntax error',line)
    return para

def GetParameter(userpara=None):
    if userpara is None:
        return para

    for key, value in userpara.items():
        para[key] = value
    return para

def ValidateParameter():
    #PATH_LANGUAGE
    if False == isdir(para['PATH_LANGUAGE']):
        raise Exception('PATH_LANGUAGE directory does not exist.')
    #INPUT_LANGUAGE
    if para['INPUT_LANGUAGE'] not in GetLanguages(para['PATH_LANGUAGE']):
        raise Exception('INPUT_LANGUAGE', para['INPUT_LANGUAGE'], 'unknown')
    #INPUT_DIALECT
    if para['INPUT_LANGUAGE'] + '/' + \
       para['INPUT_DIALECT'] not in GetDialects(para['PATH_LANGUAGE']):
        raise Exception('INPUT_DIALECT', para['INPUT_DIALECT'], 'unknown')
    #INPUT_MACHINE
    if para['INPUT_LANGUAGE'] + '/' + \
       para['INPUT_DIALECT']  + '/' + \
       para['INPUT_MACHINE'] not in GetMachines(para['PATH_LANGUAGE']):
        raise Exception('INPUT_MACHINE', para['INPUT_MACHINE'], 'unknown')
    #OUTPUT_LANGUAGE
    if para['OUTPUT_LANGUAGE'] not in GetLanguages(para['PATH_LANGUAGE']):
        raise Exception('OUTPUT_LANGUAGE', para['OUTPUT_LANGUAGE'], 'unknown')
    #OUTPUT_DIALECT
    if para['OUTPUT_LANGUAGE'] + '/' + \
       para['OUTPUT_DIALECT'] not in GetDialects(para['PATH_LANGUAGE']):
        raise Exception('OUTPUT_DIALECT', para['OUTPUT_DIALECT'], 'unknown')
    #OUTPUT_MACHINE
    if para['OUTPUT_LANGUAGE'] + '/' + \
       para['OUTPUT_DIALECT']  + '/' + \
       para['OUTPUT_MACHINE'] not in GetMachines(para['PATH_LANGUAGE']):
        raise Exception('OUTPUT_MACHINE', para['OUTPUT_MACHINE'], 'unknown')

    

def GetLanguages(path):
    """
    Returns installed languages.
    """
    files = []
    for f in listdir(path):
        if isfile(join(path, f)) and \
           re.search("^_{1}[A-Z]{1}\w*\.py$",f) is not None:
            files.append(f[1:-3])
    return files

def GetDialects(path):
    """
    Returns installed languages.
    """
    langs = GetLanguages(path)
    files = []
    for lang in langs:
        dirs = join(path,lang)
        for f in listdir(dirs):
            if isfile(join(dirs, f)) and \
               re.search("^_{1}[A-Z]{1}\w*\.py$",f) is not None:
                files.append(lang + '/' + f[1:-3])
    return files
    
def GetMachines(path):
    """
    Returns installed languages.
    """
    dials = GetDialects(path)
    files = []
    for dial in dials:
        dirs = path + '/' + dial
        for f in listdir(dirs):
            if isfile(join(dirs, f)) and \
               re.search("^_{1}[A-Z]{1}\w*\.py$",f) is not None:
                files.append(dial + '/' + f[1:-3])
    return files
    
para = {'PATH_LANGUAGE' : './Languages',
        'INPUT_LANGUAGE' : None,
        'INPUT_DIALECT' : None,
        'INPUT_MACHINE' : None,
        'OUTPUT_LANGUAGE' : None,
        'OUTPUT_DIALECT' : None,
        'OUTPUT_MACHINE' : None,
        'NUMBER' : 'YES',
        'USE_SUBROUTINES' : 'NO'}
