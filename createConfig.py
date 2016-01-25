#!/usr/bin/env python
# -*- coding: utf8 -*-
import json
from difflib import SequenceMatcher
import csv
import re
from tkinter import filedialog
import tkinter as tk
import os

def load_json_conf(confFile):
	with open(confFile) as f:
		jsonData = json.load(f)
		return jsonData

def seeDiff(jsonData,listOfPosts):
	for postConvertFrom in listOfPosts:
	    #print("!!!!!!",type(postConvertFrom),repr(postConvertFrom))  #('Деркул', 'смтБiловодськ')
	    for sheet in jsonData:
	        postNameInSheetOrigin = jsonData[sheet][1]
	        sheetTuple = tuple(re.sub(r'[-_]',' ',sheet).split())
	        #print(type(sheet),repr(sheet))         #<class 'str'> 'КазТор-Слов'
	        try:
	            postNameInSheet = re.sub(r'[-_]',' ',postNameInSheetOrigin[postNameInSheetOrigin.index("р.") + 2:]).split()
	        except ValueError:
	            #print("Exception!!!!!!!!!",sheet,postNameInSheet)
	            postNameInSheet = re.sub(r'[-_]',' ',postNameInSheetOrigin).split()
	            #print(postNameInSheet)
	        #print (repr(postNameInSheet))                #'КазеннийТорець-м.Словянськ'
	        rmList = []
	        rnList = []
	        for i,chunk in enumerate(postConvertFrom[0]):
	            try:
	                m0 = SequenceMatcher(None,chunk,postNameInSheet[i])
	                #print(chunk,postNameInSheet)
	                rmList.append(m0.ratio())
	            except IndexError:
	                pass
	            try:
	                n0 = SequenceMatcher(None,chunk,sheetTuple[i])
	                #print("CHUNK###",chunk,sheetTuple)
	                rnList.append(n0.ratio())
	            except IndexError:
	                pass
	        #print(rmList,rnList)
	        rn = sum(rnList)
	        rm = sum(rmList)
	        mainRatio = rm + rn
	        #print(postConvertFrom,"------","===>",mainRatio)    #('Деркул', 'смтБiловодськ') ------ ===> 0.0
	        if mainRatio > 2.55:
	        	#print(("RATIO IS ", mainRatio, sheet, postConvertFrom[1]))
	        	yield (sheet, postNameInSheetOrigin ,postConvertFrom[1], postConvertFrom[2], postConvertFrom[3])

def write_posts_names_to_config(sheetesAndPosts):              # sheetesAndPosts varieble must be a generator
    for pair in sheetesAndPosts:
    	if pair[2] not in jsonData[pair[0]]:
    		jsonData[pair[0]].append(pair[2])
    		print(pair[2],pair[3])
    with open("configure.json","w") as f:
    	#print(jsonData)
    	json.dump(jsonData, f, ensure_ascii=False, indent=4)
    	for data in jsonData:
    		print(data)
    	print(len(jsonData))

def write_index_year_table(indexYearPost):                      # indexYearPost must be a generator
    #for i in indexYearPost:print(i)
    with open("indexYearPost.csv","w",newline='') as csvfile:
    	headline = ['year'] + [x for x in range(1,46)]
    	writer = csv.writer(csvfile,delimiter=',', lineterminator='\n')
    	writer.writerow(headline)
    	# for i in indexYearPost:
    	#     writer.writerow(i)
    	    #print(i)
    	writer.writerows(indexYearPost)

def walking(root):
    for folder in os.listdir(root):
        try:
            folderInteger = int(folder)
        except ValueError:
        	continue
        for dirPath, dirs, files in os.walk(os.path.join(root,folder)):
            files.sort()
            for fileSingle in files:
                if fileSingle[-3:] == 'xls' or fileSingle[-4:] == 'xlsx':
                    print ('---PASS',fileSingle)
                else:
                    #print(os.path.join(dirPath,fileSingle),folderInteger)
                    yield (os.path.join(dirPath,fileSingle),folderInteger)
            #print(dirPath)

def parseDoc(filenameGenerator):
	for filename,year in filenameGenerator:
	    with open(filename, 'rb') as f:
	    	counter = 0
	    	mark = False
	    	for r in f:
	    		if not mark:
	    		    if not re.search('[Тт]аблиц[ая] ?1.12',r.decode('ibm866')) and not re.search('[Тт]емпература вод[иы]',r.decode('ibm866')):
	    		        counter += 1
	    		        if counter == 4:break
	    		        continue
	    		    else:mark = True
	    		else:
	    			if " р." in r.decode('ibm866'):
	    			    try:
	    			        postIndex = int((re.search('[0-9]{5}',r.decode('ibm866'))).group(0))
	    			        #print (postIndex)
	    			    except AttributeError:
	    			        postIndex = None
	    			    if postIndex and postIndex in indexList:
	    			        continue
	    			    else:
	    			        postName = r.decode('ibm866')[r.decode('ibm866').index(" р.") + 1:].rstrip().replace(' ','')
	    			        postNameTuple = tuple(postName[2:].split('-'))
	    			        #print(repr(postNameTuple))
	    			        yield (postNameTuple, postName, filename, postIndex, year)
	    			elif re.search('[Кк]анал',r.decode('ibm866')):
	    			    try:
	    			        postIndex = int((re.search('[0-9]{5}',r.decode('ibm866'))).group(0))
	    			    except AttributeError:
	    			        postIndex = None
	    			    if postIndex and postIndex in indexList:
	    			        continue
	    			    elif None not in indexList and postIndex == None or None in indexList:
	    			        postName = r.decode('ibm866')[r.decode('ibm866').index("анал") + 1:].rstrip().replace(' ','')
	    			        postNameTuple = tuple(postName[3:].split('-'))
	    			        #print(repr(postNameTuple))
	    			        yield (postNameTuple, postName, filename, postIndex, year)

def parseDocRowList(filenameGenerator):
	for_one_year_list = []
	filenameGenerator = list(filenameGenerator)
	count = 1
	for filenameyear in filenameGenerator:
	    if len(for_one_year_list) == 0:
	        for_one_year_list.append(filenameyear[1])
	    elif filenameyear[1] not in for_one_year_list and len(for_one_year_list) != 0:
	        yield for_one_year_list
	        for_one_year_list = []
	        for_one_year_list.append(filenameyear[1])
	    with open(filenameyear[0], 'rb') as f:
	    	print(filenameyear[0])
	    	for r in f:
	    		if " р." in r.decode('ibm866'):
	    		    postIndex = int((re.search('[0-9]{5}',r.decode('ibm866'))).group(0))
	    		    #print (postIndex)
	    		    postName = r.decode('ibm866')[r.decode('ibm866').index(" р.") + 1:].rstrip().replace(' ','')
	    		    for_one_year_list.append(postName)
	    		    #postNameTuple = tuple(postName[2:].split('-'))
	    		    #print(repr(postNameTuple))
	    		    #yield (postNameTuple, postName, filename, postIndex, year)
	    		elif re.search('[Кк]анал',r.decode('ibm866')):
	    		    postIndex = int((re.search('[0-9]{5}',r.decode('ibm866'))).group(0))
	    		    postName = r.decode('ibm866')[r.decode('ibm866').index("анал") + 1:].rstrip().replace(' ','')
	    		    for_one_year_list.append(postName)
	    		    #postNameTuple = tuple(postName[3:].split('-'))
	    		    #print(repr(postNameTuple))
	    		    #yield (postNameTuple, postName, filename, postIndex, year)
	    	#print(for_one_year_list)
	    	if count == len(filenameGenerator):
	    		yield for_one_year_list
	    	else:
	    		count += 1
	    #yield for_one_year_list


def choosePath():
    root = tk.Tk()
    root.withdraw()
    root = filedialog.askdirectory(title="Select A Folder", mustexist=1)
    return root

if __name__ == "__main__":
    # parseDocFilename = "T78281.V3"
    # parseDocFilename1 = "Tabl1.12 sivDon"
    # parseDocFilename2 = "T78281.txt"
    #seeDiff("configure.json",parseDoc(parseDocFilename2))
    root = choosePath()
    if root:
        jsonData = load_json_conf("configure.json")
        indexList = [jsonData[x][0] for x in jsonData]
        #write_index_year_table(parseDocRowList(walking(root)))
        write_posts_names_to_config(seeDiff(jsonData,parseDoc(walking(root))))
        print(indexList)
        print("Chosen path to dataBase is: ",root)
    print("Exit.")
    #seeDiff("configure.json")
    # for i in parseDoc("Tabl1.12 sivDon"):
    # 	print(i)