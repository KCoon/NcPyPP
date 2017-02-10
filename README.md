# NcPyPP
Macro postprocessor for cnc machining

## Flags
parameter           | description
--------------------|------------
-n --number         | numbering lines
-l --lang <value>   | nc language ('heidenhain' short'hh', 'iso')
-d --dial <value>   | dialect ('itnc', 'tnc kern', 'M700')
-m --machine <value>| machine ('hermle c40', 'foehrenbach fumg')
-s --sub            | use subprograms


|
|-- detect language/ dialect
|
|-- include subprograms
|
|-- replace line jumps with labels
|
|-- replace macros with nc-code
|
|-- renumber
|
|-- replace labels with lines
