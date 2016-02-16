===========
hydroparser
===========


Add a short description here!


Description
===========

A LONGER DESCRIPTION OF YOUR PROJECT GOES HERE...


Flexible invocation
=================== 

## The application can be run right from the source directory, in two different ways: 


# 1. Treating the hydroparser directory as a package and as the main script:

   $ python -m hydroparser arg1 arg2
   Executing hydroparser version 0.1.3.

# 2. Using the hydroparser-runner.py wrapper:

   $ ./hydroparser-runner.py arg1 arg2
   Executing hydroparser version 0.1.3.

## Installation sets up hydroparser command

Situation before installation:

> $ hydroparser
> bash: hydroparser: command not found

# 1. Installation right from the source tree:
Go to the root folder of this project,where is setup.py and:

> $ python setup.py install

# 2 . Installation from github repository:

# install by branch names
> $ pip install git+git://github.com/sashkozab/hydroparser.git@master#egg=hydroparser

# also you can install version you want
> $ pip install git+git://github.com/sashkozab/hydroparser.git@v0.1.3#egg=hydroparser

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

> $ hydroparser arg1 arg2
> Executing hydroparser version 0.1.3.

