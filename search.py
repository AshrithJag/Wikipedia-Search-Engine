import math
import sys
import os
from nltk.stem.porter import *
import re
import operator

meta_data = []
doc_dict = {}
alpha = ['i','r','e','b','c','t']
rankt = 10
rankb = 1
rankc = 4
ranki = 2
rankr = 5
ranke = 5
def searching(word,field):

    global meta_data
#    global doc_dict
    global alpha
    global rankt , rankc , ranki , rankr , ranke , rankb
        
    doc = -1

    for temp in range(len(meta_data)-1):
        if (str(word) > str(meta_data[temp][0])) and (str(word) < str(meta_data[temp+1][0])):
            doc = int(meta_data[temp][1])
            break

    posting = []
    doc_id = []
    if doc != -1: 
        file_doc = open('./Index/'+str(doc),'r')
        file_doc = file_doc.readlines()
        for line in file_doc:
            temp = line.split(' ')
            if word == temp[0]:
                temp[1] = temp[1].rstrip()
                if '|' in temp[1]:
                    posting = temp[1].split('|')
                else:
                    posting.append(temp[1]) 

#       Getting Doc_ids
    for element in posting:
        minm = []
        if len(element.split('t')) != 1:
            minm.append(int(element.index('t')))
        if len(element.split('r')) != 1:
            minm.append(int(element.index('r')))
        if len(element.split('i')) != 1:
            minm.append(int(element.index('i')))
        if len(element.split('b')) != 1:
            minm.append(int(element.index('b')))
        if len(element.split('e')) != 1:
            minm.append(int(element.index('e')))
        if len(element.split('c')) != 1:
            minm.append(int(element.index('c')))

        minm = min(minm)
        num = ''
        for init in range(minm):
            num += element[init]
        
        doc_id.append(int(num))
        
#    print doc_id
            
    if field == 'title' and doc != -1: 
        for element in range(len(posting)):
            if 't' in posting[element]:
#                print element
                init = str(posting[element]).index('t')
                temp = init + 1
                num = ''
                while temp != len(posting[element]) and posting[element][temp] not in alpha:
                    num += posting[element][temp]
                    temp += 1
                num = int(num)

                #frequency
                if doc_id[element] not in doc_dict:
                    doc_dict[doc_id[element]] = num*rankt
                else:
                    doc_dict[doc_id[element]] += num*rankt

#        print doc_dict
            
    elif field == 'body' and doc != -1: 
        for element in range(len(posting)):
            if 'b' in posting[element]:
#                print element
                init = str(posting[element]).index('b')
                temp = init + 1
                num = ''
                while temp != len(posting[element]) and posting[element][temp] not in alpha:
                    num += posting[element][temp]
                    temp += 1
                num = int(num)

                #frequency
                if doc_id[element] not in doc_dict:
                    doc_dict[doc_id[element]] = num*rankb
                else:
                    doc_dict[doc_id[element]] += num*rankb

    elif field == 'category' and doc != -1: 
        for element in range(len(posting)):
            if 'c' in posting[element]:
#                print element
                init = str(posting[element]).index('c')
                temp = init + 1
                num = ''
                while temp != len(posting[element]) and posting[element][temp] not in alpha:
                    num += posting[element][temp]
                    temp += 1
                num = int(num)

                #frequency
                if doc_id[element] not in doc_dict:
                    doc_dict[doc_id[element]] = num*rankc
                else:
                    doc_dict[doc_id[element]] += num*rankc

    elif field == 'infobox' and doc != -1: 
        for element in range(len(posting)):
            if 'i' in posting[element]:
#                print element
                init = str(posting[element]).index('i')
                temp = init + 1
                num = ''
                while temp != len(posting[element]) and posting[element][temp] not in alpha:
                    num += posting[element][temp]
                    temp += 1
                num = int(num)

                #frequency
                if doc_id[element] not in doc_dict:
                    doc_dict[doc_id[element]] = num*ranki
                else:
                    doc_dict[doc_id[element]] += num*ranki

    elif field == 'reference' and doc != -1: 
        for element in range(len(posting)):
            if 'r' in posting[element]:
#                print element
                init = str(posting[element]).index('r')
                temp = init + 1
                num = ''
                while temp != len(posting[element]) and posting[element][temp] not in alpha:
                    num += posting[element][temp]
                    temp += 1
                num = int(num)

                #frequency
                if doc_id[element] not in doc_dict:
                    doc_dict[doc_id[element]] = num*rankr
                else:
                    doc_dict[doc_id[element]] += num*rankr

    elif field == 'external' and doc != -1: 
        for element in range(len(posting)):
            if 'e' in posting[element]:
#                print element
                init = str(posting[element]).index('e')
                temp = init + 1
                num = ''
                while temp != len(posting[element]) and posting[element][temp] not in alpha:
                    num += posting[element][temp]
                    temp += 1
                num = int(num)

                #frequency
                if doc_id[element] not in doc_dict:
                    doc_dict[doc_id[element]] = num*ranke
                else:
                    doc_dict[doc_id[element]] += num*ranke

    elif field == 'all' and doc != -1:
        for element in range(len(posting)):
            if 't' in posting[element]:
#                print element
                init = str(posting[element]).index('t')
                temp = init + 1
                num = ''
                while temp != len(posting[element]) and posting[element][temp] not in alpha:
                    num += posting[element][temp]
                    temp += 1
                num = int(num)

                #frequency
                if doc_id[element] not in doc_dict:
                    doc_dict[doc_id[element]] = num*rankt
                else:
                    doc_dict[doc_id[element]] += num*rankt

            if 'b' in posting[element]:
#                print element
                init = str(posting[element]).index('b')
                temp = init + 1
                num = ''
                while temp != len(posting[element]) and posting[element][temp] not in alpha:
                    num += posting[element][temp]
                    temp += 1
                num = int(num)

                #frequency
                if doc_id[element] not in doc_dict:
                    doc_dict[doc_id[element]] = num*rankb
                else:
                    doc_dict[doc_id[element]] += num*rankb

            if 'c' in posting[element]:
#                print element
                init = str(posting[element]).index('c')
                temp = init + 1
                num = ''
                while temp != len(posting[element]) and posting[element][temp] not in alpha:
                    num += posting[element][temp]
                    temp += 1
                num = int(num)

                #frequency
                if doc_id[element] not in doc_dict:
                    doc_dict[doc_id[element]] = num*rankc
                else:
                    doc_dict[doc_id[element]] += num*rankc

            if 'i' in posting[element]:
#                print element
                init = str(posting[element]).index('i')
                temp = init + 1
                num = ''
                while temp != len(posting[element]) and posting[element][temp] not in alpha:
                    num += posting[element][temp]
                    temp += 1
                num = int(num)

                #frequency
                if doc_id[element] not in doc_dict:
                    doc_dict[doc_id[element]] = num*ranki
                else:
                    doc_dict[doc_id[element]] += num*ranki

            if 'r' in posting[element]:
#                print element
                init = str(posting[element]).index('r')
                temp = init + 1
                num = ''
                while temp != len(posting[element]) and posting[element][temp] not in alpha:
                    num += posting[element][temp]
                    temp += 1
                num = int(num)

                #frequency
                if doc_id[element] not in doc_dict:
                    doc_dict[doc_id[element]] = num*rankr
                else:
                    doc_dict[doc_id[element]] += num*rankr

            if 'e' in posting[element]:
#                print element
                init = str(posting[element]).index('e')
                temp = init + 1
                num = ''
                while temp != len(posting[element]) and posting[element][temp] not in alpha:
                    num += posting[element][temp]
                    temp += 1
                num = int(num)

                #frequency
                if doc_id[element] not in doc_dict:
                    doc_dict[doc_id[element]] = num*ranke
                else:
                    doc_dict[doc_id[element]] += num*ranke

#    print doc_dict
       
        
if __name__ == "__main__":


    path_query = sys.argv[1]
    path_index = sys.argv[2]
    index_file = open(str(path_index)).readlines()
    query_file = open(str(path_query)).readlines()
    stopwords = open('./src/stoplist.txt','r+').readlines()
    for i in range(len(stopwords)):
        stopwords[i] = stopwords[i].split('\n')[0]
    
    while '' in stopwords:
        stopwords.remove('')

    for i in range(len(query_file)):
        query_file[i] = query_file[i].split('\n')[0]


    for element in index_file:
        element = element.split('|')
        for temp in element:
            temp = temp.split(',')
            if temp[1][len(temp[1])-1] == '\n':
                temp[1] = temp[1][:len(temp[1])-1]
            meta_data.append(temp)

    for i in range(int(query_file[0])):
        query = str(query_file[i+1]).split()
        doc_dict = {}
        word_flag = [0]*(len(query))

        stemmer = PorterStemmer()
        for word1 in query:
            doc = -1
            if str(word1) in stopwords:
                pass
            word1 = str(word1).lower()
            word1 = str(stemmer.stem(word1))
            if word1[:2] == 't:':
                searching(word1[2:],'title')
            elif word1[:2] == 'b:':
                searching(word1[2:],'body')
            elif word1[:2] == 'c:': 
                searching(word1[2:],'category')
            elif word1[:2] == 'i:':
                searching(word1[2:],'infobox')
            elif word1[:2] == 'r:':
                searching(word1[2:],'reference')
            elif word1[:2] == 'e:':
                searching(word1[2:],'external')
            else:
                searching(word1 , 'all')
#            print word1

        print "--------------------QUERY "+ str(i+1) +"-------------------"
        sorted_dict = sorted(doc_dict.items() , key=operator.itemgetter(1))
        top_ten = sorted_dict[len(sorted_dict)-10 : len(sorted_dict)]
        f = open('./src/min_id.txt','r').readline()
        f = int(f)
        g = open('./src/Titles.txt','r').readlines()
        finale = []
        if top_ten:
            for i in range(10):
                for j in g:
                    if (str(f+top_ten[i][0])) in j:
                        finale.append(j)
                        break
            finale = finale[::-1] 
            for element in finale:
                print element
        else:
            print '****************\: No Matches found :/******************'
