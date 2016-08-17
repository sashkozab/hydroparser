===========
hydroparser
===========


This is a little project for hydrology science. The goal is to parse some information, that we need, from xlsx,doc,txt and similar formats to
excel table prepared for this data. And, we have automatically build charts option inside another excel file.


Description
===========

A LONGER DESCRIPTION WILL BE HERE LATER...


Flexible invocation
===================

## The application can be run right from the source directory, in two different ways:

# 1. Treating the hydroparser directory as a package and as the main script:

$ python -m hydroparser arg1 arg2 Executing hydroparser version 0.1.3.

# 2. Using the hydroparser_runner.py wrapper:

$ ./hydroparser_runner.py arg1 arg2 Executing hydroparser version 0.1.3.


## Installation sets up hydroparser command

Situation before installation:

   $ hydroparser
   bash: hydroparser: command not found

# 1. Installation right from the source tree: Go to the root folder of this project,where is setup.py and:

    $ python setup.py install

# 2 . Installation from github repository:

# install by branch names

     pip install git+git://github.com/sashkozab/hydroparser.git@master#egg=hydroparser

# also you can install version you want

     pip install git+git://github.com/sashkozab/hydroparser.git@v0.1.3#egg=hydroparser

# or by commit

     pip install git+git://github.com/sashkozab/hydroparser.git@dbbd99ad1877c9b2c409b9ec8eebe023bc87f40c#egg=hydroparser

# or simple just

     pip install git+git://github.com/sashkozab/hydroparser.git@#egg=hydroparser

# Here are another supported forms by git:

     pip install git+ssh://github.com/sashkozab/hydroparser.git@#egg=hydroparser

     pip install git+https://github.com/sashkozab/hydroparser.git@#egg=hydroparser


More information about installing by pip from git and other you can find there: https://pip.pypa.io/en/latest/reference/pip_install/#vcs-support

# Now, the hydroparser command is available:

   $ hydroparser arg1 arg2 > Executing hydroparser version 0.1.3.



Short Usage
===========

Usage: hydroparser [OPTION]...[ARGUMENT]...

Options:
  -v, --version          Print current version of this aplication.
  -h, --help             Show this usage options.
  -g, --generate-conf    Generate configuration json file with list of sheet,postname,index.
  -c, --create-conf      Add headers that don't have post index to exist configuration json file. Always check configuration file after this!!
  -r, --ratio=NUMBER     This option for select words difference ratio,just needed in case when some post indexes does not exist.
                         It is addition for (-c,--create-conf) option.DEFOULT value is 2.55. Be careful to change it.
                         Be cautios to check configuration json file after this!

Convertion options:
  -t, --temperature      Search in data base the temperature of water and add actual data to exist .xlsx file with excel sheets.

Build chart options:
  -b, --build-charts     Build charts inside xlsx file.


Examples:
  hydroparser -g                    Generate only configuration file.
  hydroparser -gc --ratio 2.6       Generate and add headers to configuration file with ratio equal to 2.6
  hydroparser -gct                  Generate,add headers to configuration file and parse temperature of water in data base with adding to .xlsx main file.
  hydroparser -h                    Show this screen.
  hydroparser -gctb                 Generate,add headers to configuration file and parse temperature of water in data base with adding to .xlsx main file.
                                    And finally, build charts in separate xlsx file.
  hydroparser -b                    Just build charts in xlsx file.


Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/sashkozab/hydroparser 