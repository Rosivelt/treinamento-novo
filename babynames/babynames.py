#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
    lista_nome = []
    f = open(filename,'rU')
    for line in f:
        if re.search(r'h3',line):
            ano = line[-10:-6]
        elif re.search(r'<tr\salign="right"><td>\d</td><td>\w+</td><td>\w+</td>',line):
            grupos = re.search('<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>',line)
            lista_nome.append(grupos.group(2)+' '+grupos.group(1))
            lista_nome.append(grupos.group(3)+' '+grupos.group(1))
    lista_nome.sort()
    lista_nome.insert(0,ano)
    return lista_nome

def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
    args = sys.argv[1:]
    print args
    if not args:
        print 'usage: [--summaryfile] file [file ...]'
        sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
    summary = False
    extracao = []
    qtd = 0
    i = 0
    if args[0] == '--summaryfile':
        summary = True
        del args[0]
        if not args:
            print 'usage: [--summaryfile] file [file ...]'
            sys.exit(1)
        else:
            for arq in args:
                extracao.append(extract_names(arq))
                qtd += 1
            if summary == True:
                while i < qtd:
                    print extracao[i]
                    i+=1

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  #
if __name__ == '__main__':
    main()

