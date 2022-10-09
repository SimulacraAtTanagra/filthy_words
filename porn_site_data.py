# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 10:19:28 2022

@author: shane
"""
"""tags and categories sources from xnxx, xhamster, thothub, pornhub, etc"""

#cleaning data of symbols, spaces

def clean_item(item,numbers=None):
	replacements=[")","(","[","]",":",";","!","@","#","$","%","^","&","*",",",
			   ".","_","/","|","?","'",'"']
	numbers_=['1','2','3','4','5','6','7','8','9','0']
	if numbers:
		replacements=replacements+numbers_
	for x in replacements:
		item=item.replace(x," ")
	return(item.strip().lower())
def clean_item2(item,numbers=None):
	replacements=[")","(","[","]",":",";","!","@","#","$","%","^","&","*",",",
			   ".","_","/","|","?","'",'"']
	numbers_=['1','2','3','4','5','6','7','8','9','0']
	if numbers:
		replacements=replacements+numbers_
	for x in replacements:
		item=item.replace(x,"")
	return(item.strip().lower())


def clean_data(datastr):
	#split into list
	listofdata=datastr.split('\n')
	dataset=set()
	for item in listofdata:
		dataset.add(clean_item(item))
	return(dataset)

def find_views(datastr,key=None):
	import re
	if key:
		return(clean_item2(datastr[len(key):]))
	else:
		views=re.findall(r"[a-z]+([\d]+[^a-z]+$)",datastr)
	if len(views)>0:
		return(clean_item2(views[0]))
	else:
		return(None)

def clean_ph_data(datastr):
	#split into list
	listofdata=datastr.split('\n')
	dataset=set()
	finaldata=set()
	for item in listofdata:
		dataset.add(clean_item2(item,numbers=True))
	dataset=[i for i in dataset if len(i)>1]
	for item in dataset:
		counter=0
		for i in listofdata:
			if item in i:
				try:
					counter+=int(clean_item2(find_views(i,key=item)))
				except Exception as e:
					#print(e)
					pass
		tup=tuple([item,counter])
		finaldata.add(tup)
	return(finaldata)

def str_to_list(datastr):
	#split into list
	listofdata=datastr.split('\n')
	return(listofdata)
def list_to_file(outfile,list_):
	with open(outfile, 'w',encoding="utf-8") as fp:
	    for item in list_:
	        # write each item on a new line
	        fp.write("%s\n" % item)
	    print('Done')
		
def read_list_from_file(infile):
	list_=[]
	with open(infile, 'r') as fp:
	    for line in fp:
	        # remove linebreak from a current name
	        # linebreak is the last character of each line
	        x = line.replace('\n',"")
	        # add current item to the list
	        list_.append(x)
	return(list_)

if __name__=="__main__":
	phdata=[i for i in list(clean_data(phdata)) if len(i)>1]
	
	
	list_to_file("C:/Users/shane/desktop/projects/programs/thothubclean.txt",thothubdata)
	list_to_file("C:/Users/shane/desktop/projects/programs/xnxxclean.txt",[list(i) for i in xdata_2])
	list_to_file("C:/Users/shane/desktop/projects/programs/xhamsterclean.txt",xhamdata)
	list_to_file("C:/Users/shane/desktop/projects/programs/pornhubclean.txt",phdata)