===========
hydroparser
===========


Add a short description here!


Description
===========

A LONGER DESCRIPTION OF YOUR PROJECT GOES HERE...


Flexible invocation
=================== 

##  The application can be run right from the source directory, in two different ways:


# 1. Treating the hydroparser directory as a package and as the main script:

   $ python -m hydroparser arg1 arg2
   Executing hydroparser version 0.1.2.

# 2. Using the hydroparser-runner.py wrapper:

   $ ./hydroparser-runner.py arg1 arg2
   Executing hydroparser version 0.1.2.

## Installation sets up hydroparser command

Situation before installation:

   $ hydroparser
    bash: hydroparser: command not found

# 1. Installation right from the source tree:
Go to the root folder of this project,where is setup.py and:

> $ python setup.py install

# 2 . Installation from github repository:

# install by branch names
> $ pip install git+git://github.com/sashkozab/hydroparser.git@master#egg=hydroparser

# also you can install version you want
> $ pip install git+git://github.com/sashkozab/hydroparser.git@v0.1.2#egg=hydroparser

# or by commit
> pip install git+git://github.com/sashkozab/hydroparser.git@dbbd99ad1877c9b2c409b9ec8eebe023bc87f40c#egg=hydroparser

# or simple just
> pip install git+git://github.com/sashkozab/hydroparser.git@#egg=hydroparser

# Here are another supported forms by git:
> pip install git+ssh://github.com/sashkozab/hydroparser.git@#egg=hydroparser
> pip install git+https://github.com/sashkozab/hydroparser.git@#egg=hydroparser

More information about installing by pip from git and other you can find there:
https://pip.pypa.io/en/latest/reference/pip_install/#vcs-support

# Now, the hydroparser command is available:

>  $ hydroparser arg1 arg2
>  Executing hydroparser version 0.1.2.

Additional instruction
=================

In some cases,for example you have Windows,you can have problem with installing NumPy library. Becaouse, you need to have Microsoft Visual C++ Compiler for Python 3.4
So you can install Microsoft Visual C++ 2010 Express, download here http://download.microsoft.com/download/1/D/9/1D9A6C0E..

Or you can do preinstall numpy module from wheel: download it from http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy and install via pip command from your local machine. Remember,you need version for python 3.
