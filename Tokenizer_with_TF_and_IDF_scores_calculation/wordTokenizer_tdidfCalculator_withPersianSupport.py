import re
import os
import pandas as p
import math


#this tuple is the right order of persian alphabet in case of using it in BubleSort
persian_alphabet_order = ("ا","ب","پ","ت","ث","ج","چ","ح"
                         ,"خ","د","ذ","ر","ز","ژ","س","ش"
                         ,"ص","ض","ط","ظ","ع","غ","ف","ق"
                         ,"ک","گ","ل","م","ن","و","ه","ی",)                         

text = [] #list of simple input texts
token_list = [] # list of tokens from text (all sorted in that)
num_list = [] # list of nums in text for good sorting we seperate these
english_token = [] # list of english in text for good sorting we seperate these
oneD_all_unique = [] #an one diension list of all tokens uniqued in token_list
worddic = {} #one dictionary {0:{oned_all_unique} , 1:{}} that shows number of words in text 
worddic_ls = [] # list for uppon dictionary [{},{}]
link_ls= []



#getting the text file
def loadFile():
	#add your text files location
    my_input_files = os.listdir("texts/")
    for text_files in my_input_files:
        with open('texts/'+text_files,'r',encoding = 'utf-8') as docs:
            text.append(docs.read())


#this part is for replacing trash unicodes with correct one or Normalization        
def normalize():
    alef = "ا"
    h = "ح"
    d = "د"
    s="ص"
    ain = "ع"
    k = "ک"
    gh = "گ"
    n = "ن"
    v = "و"
    he = "ه"
    ye = "ی"
    for i in range(len(text)):
        text[i] = re.sub(r"(\u200c)", "", text[i])
        text[i] = re.sub(r"([إآأ])", alef, text[i])
        text[i] = re.sub(r"([ځ])", h, text[i])
        text[i] = re.sub(r"([ڍ])", d, text[i])
        text[i] = re.sub(r"([ڝ])", s, text[i])
        text[i] = re.sub(r"([ݝ])", ain, text[i])
        text[i] = re.sub(r"([ڪك])", k, text[i])
        text[i] = re.sub(r"([ڲ])", gh, text[i])
        text[i] = re.sub(r"([ݧ])", n, text[i])
        text[i] = re.sub(r"([ؤۆ])", v, text[i])
        text[i] = re.sub(r"([ةۀ])", he, text[i])
        text[i] = re.sub(r"([يئ])", ye, text[i])    


#in this part with regular expression we get the words in the text,
#new dfa only for persian unicodes
def tokenize():
    for j in range(len(text)):
        token_list.append(re.findall("[\u0621-\u0628\u062A-\u063A\u0641-\u0642\u0644-\u0648\u064E-\u0651\u0655\u067E\u0686\u0698\u06A9\u06AF\u06BE\u06CC]+[‌]*[\u0621-\u0628\u062A-\u063A\u0641-\u0642\u0644-\u0648\u064E-\u0651\u0655\u067E\u0686\u0698\u06A9\u06AF\u06BE\u06CC]+",text[j]))
        #dfa for digits
        link_ls.append(re.findall(r"(?:https?:\/\/)?(?:www\.)?[-a-zA-Z0-9%._\+~#=]{1,256}\.[a-zA-Z][a-zA-Z0-9]{0,6}(?:[A-Za-z\-\/0-9_$%]*)(?:#(?:[a-zA-Z0-9]+=[a-zA-Z0-9]*,)*(?:[a-zA-Z0-9]+=[a-zA-Z0-9]*))?",text[j]))
        xx1= []
        xx1.append( re.findall(r'\b\d+\b',text[j]))
        xx = []
        xx.append(re.findall(r"[a-zA-Z]+[]*[a-zA-Z]+",text[j]))
        ll = "_".join(link_ls[j])
        zz1 = []
        zz = [] 
        for i in range(len(xx[j])):
            if(xx[j][i] not in ll):
                zz.append(xx[j][i])
        english_token.append(zz)  

        for i in range(len(xx1[j])):
            if(xx1[j][i] not in ll):
                zz1.append(xx1[j][i])
        num_list.append(zz1)
        del ll,zz,zz1,xx1,xx
    


#my custom buble sort algorithem
"""def customBubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            z=0
            #getting the order of words first letter
            num0  = persian_alphabet_order.index(arr[j][z])
            num1 = persian_alphabet_order.index(arr[j+1][z])
            #getting the size of words in case of that first letters are in the same order
            len0 = len(arr[j])
            len1 = len(arr[j+1])
            while(num0 == num1):
                z += 1
                try:
                    #comparing the next letters in case of having equal orders
                    num0  = persian_alphabet_order.index(arr[j][z])
                    num1 = persian_alphabet_order.index(arr[j+1][z])
                except:
                    #having less letter means it has lower order so with -1 it would be lower in next step 
                    if(len0<len1):
                        num0 = -1
                    else:
                        num1 = -1
            #and the last step of sorting
            if num0 > num1 :
                arr[j], arr[j+1] = arr[j+1], arr[j]"""



def sort():
    global token_list
    global english_token
    global num_list
    global oneD_all_unique
    global link_ls
    
    

    x = []
    y = []
    z = []
    zl= []

    for j in range(len(token_list)):
        english_token[j].sort()
        num_list[j].sort()
        link_ls[j].sort()
        token_list[j].sort()
        x.extend(token_list[j])
        token_list[j].extend(english_token[j])
        y.extend(english_token[j])
        token_list[j].extend(link_ls[j])
        zl.extend(link_ls[j])
        token_list[j].extend(num_list[j])   
        z.extend(num_list[j])
        
    x.sort()
    y.sort()
    z.sort()
    zl.sort()

    oneD_all_unique.extend(x)
    oneD_all_unique.extend(y)
    oneD_all_unique.extend(zl)
    oneD_all_unique.extend(z)
  
    del x,y,z,zl      
    




def mapMaker():
     wordset = list( dict.fromkeys(oneD_all_unique) )
     for i in range(len(text)):
         worddic[i] = dict.fromkeys(wordset,0)
     for i in range (len(token_list)):
        for j in range(len(token_list[i])):
            if(token_list[i][j] in worddic[i]):
                worddic[i][token_list[i][j]] += 1
     for i in range(len(worddic)):
         worddic_ls.append(worddic[i]) 



def computeTF(wordDict, token_ls):
    tfDict_ls = []
    for i in range(len(worddic)):
        tfDict = {}
        bowCount = len(token_list[i])
        for word, count in wordDict[i].items():
            tfDict[word] = count/float(bowCount)    
        tfDict_ls.append(tfDict)
    return tfDict_ls


def computeIDF(worddic_ls):
    idfDict = {}
    N = len(worddic_ls)
    idfDict = dict.fromkeys(worddic_ls[0].keys(), 0)
    global oneD_all_unique 
    oneD_all_unique = list(worddic_ls[0].keys())
    for i in range(len(idfDict)):
        count = 0
        for j in range(len(worddic_ls)):
            if(worddic_ls[j][oneD_all_unique[i]] != 0):
                count += 1
        idfDict[oneD_all_unique[i]] = float(N)/float(count)        
    return idfDict


def computeTFIDF(tf, idf):
    tfidf_ls = []
    for i in range(len(tf)):
        tfidf = {}
        for word, val in tf[i].items():
            tfidf[word] = val*idf[word]
        tfidf_ls.append(tfidf)     
    return tfidf_ls

def showBeautiful(x):
    y = []
    for i in range(len(x[0])):
        for j in range(len(x)):
            y.append(x[j][oneD_all_unique[i]])
        print(i,".",oneD_all_unique[i]+"  == ",y)
        y = []


loadFile()
normalize()
tokenize()
sort()
mapMaker()
tf_values_list = computeTF(worddic,token_list)
idf_values_dic = computeIDF(worddic_ls)
tfidf_values_dic = computeTFIDF(tf_values_list,idf_values_dic)
showBeautiful(tfidf_values_dic)


#done. Ehsan Mokhtari - april/23/2020