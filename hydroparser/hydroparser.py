#!/usr/bin/env python
# -*- coding: utf8 -*-
"""
hydroparser

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
"""

__version__ = "0.1.2"

import os, sys, getopt
from subprocess import call
from .createConfig import *
from .parsedoc import *
from .chartBuilder import build_charts

def disableWUC():
    try:
        win_unicode_console.disable()
        sys.exit()
    except (UnboundLocalError,NameError):
        sys.exit()

def main():
    if os.name == 'nt':
        import win_unicode_console
        win_unicode_console.enable()
    argv = sys.argv[1:]
    print("Executing gydroparser version {}".format(__version__))
    try:
        opts, args = getopt.getopt(argv,"vhtgcr:b",["version","help","temperature","generate-conf","create-conf","ratio=","build-charts"])
        #print (opts)
    except getopt.GetoptError:
        print (__doc__)
        disableWUC()
    xlsx = None
    pathToFiles = None
    jsonFile = None
    g = False
    c = False
    ratio = False
    t = False
    b = False
    for opt, arg in opts:
        if opt in ('-h','--help'):
            print (__doc__)
            disableWUC()
        if opt in ('-v', '--version'):
            print ("gydroparser version is {}".format(__version__))
            disableWUC()
        elif opt in ("-g", "--generate-conf"):
            g = True  
        elif opt in ("-c", "--create-conf"):
            c = True
        elif opt in ("-r", "--ratio"):
            try:
                ratio = float(arg)
            except ValueError:
                print ("Argument of (-r,--ratio) must be a number!")
                disableWUC()
        elif opt in ("-t", "--temperature"):
            t = True
        elif opt in ("-b", "--build-charts"):
            b = True
    if g:
        xlsx = choose_file()
        if xlsx:
            jsonFile = xlsx[:-5] + "_configure.json"
            generate_file(jsonFile,xlsx)
        else:
            print("File has not been chosen! Exit.")
            disableWUC()
    if c:
        if not jsonFile:
            opts = {'filetypes' : [('JSON files','.json')], 'title' : 'Select JSON configuration file you wish to work with'}
            jsonFile = choose_file(opts)
        try:
            jsonData = load_json_conf(jsonFile)
        except TypeError:
            print ("JSON file has not been chosen. Exit.")
            disableWUC()
        pathToFiles = choose_path()
        if pathToFiles:
            indexList = [jsonData[x][0] for x in jsonData]
            createObj = createConf()
            createObj.add_table_number_pattern('таблиц[ая] ?1.12')
            createObj.add_table_name_pattern('температура вод[иы]')
            if ratio:
                write_nonindex_names_to_conf(jsonData, jsonFile, pathToFiles, createObj, indexList, ratio)
            else:
                write_nonindex_names_to_conf(jsonData, jsonFile, pathToFiles, createObj, indexList)
        else:
            print ("You should chose a path to data base for this option. Exit.")
    if t:
        if not jsonFile:
            opts = {'filetypes' : [('JSON files','.json')], 'title' : 'Select JSON configuration file you wish to work with'}
            jsonFile = choose_file(opts)
        try:
            jsonData = load_json_conf(jsonFile)
        except TypeError:
            print ("JSON file has not been chosen. Exit.")
            disableWUC()
        if not xlsx:
            xlsx = choose_file()
            if not xlsx:
                print ("XLSX file has not been chosen.Exit.")
                disableWUC()
        if not pathToFiles:
            pathToFiles = choose_path()
        if pathToFiles:
            temperatureObject = ParseOneDoc(jsonData)
            temperatureObject.add_data_marker('[СCсc]е?редн.')
            temperatureObject.add_table_number_pattern('таблиц[ая] ?1.12')
            temperatureObject.add_table_name_pattern('температура вод[иы]')
            updateXLS(walkingDead(pathToFiles, temperatureObject),xlsx)
        else:
            print ("Path to files has not been choosen.Exit.")
    if b:
        if not xlsx:
            xlsx = choose_file()
            if not xlsx:
                print ("XLSX file has not been chosen.Exit.")
                disableWUC()
        build_charts(xlsx)
        print ("Charts have been build successfully! Exit.")
    disableWUC()
   

if __name__ == "__main__":
   main()