from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import nltk
import json

import math
from textblob import TextBlob as tb

with open("output_0.json") as file:
	data0=json.load(file)

with open("output_1.json") as file:
	data1=json.load(file)

with open("output_2.json") as file:
	data2=json.load(file)

with open("output_3.json") as file:
	data3=json.load(file)
#task 1  算出整個corpus每個字的term frequency 並取前300大的當作維度
corpus=[]

with open("movie_lines.txt","r",encoding="windows-1252") as file:
	corpus=file.readlines()


tokens = nltk.word_tokenize(sentence)

data=[]
sentence_numbers=0
a=0
tf
vocabulary={}
for x in range(0,4):
	with open("output_"+str(x)+".json") as file:
		data=json.load(file)
	for id, object in data.items():
		try:
			for word in object[0]["tokens"]:
				if(word["word"].lower() in vocabulary):
					vocabulary[word["word"].lower()]=vocabulary[word["word"].lower()]+1
				else:
					vocabulary[word["word"].lower()]=1
			a=a+1		
		except:
			print("n")

idf={}
for id, object in vocabulary.items():
	idf[id]=math.log(a/object,10)

vec_name=sorted(idf,key=idf.__getitem__,reverse=True)[1:300]

def tfidf(toke_result,vect):
	cal_tf={}
	cal_tfidf={}
	for vec in vect:
		cal_tf[vec]=0
		for word in toke_result[0]["tokens"]:
			if(vec in word["word"]):
				cal_tf[vec]=cal_tf[vec]+1
	for id,object in cal_tf.items() :
		cal_tfidf[id]=object*idf[id]
	return cal_tfidf

with open("task_1.txt","w") as file:
    for name in vec_name:
        file.write(name+'|')
    file.write('\n')
    for name in vec_name:
        file.write(str(idf[name])+',')
    file.write('\n')


file=open("task_1.txt","a")
[8672,47513,106189,155825,175846,227942,249352,268554,282716]
res=tfidf(data2["282716"],vec_name)
for id,object in res.items():
	file.write(str(object)+',')
file.write("\n")
file.close()
#task 2 算出斷詞完的term frequency(包含詞性)，然後做一樣的東西
vocabulary_t2={}
a_t2=0
for x in range(0,4):
	with open("output_"+str(x)+".json") as file:
		data=json.load(file)
	for id, object in data.items():
		try:
			for word in object[0]["tokens"]:
				print(word["word"]+word["pos"])
				if(word["word"].lower()+"/"+word["pos"] in vocabulary_t2):
					vocabulary_t2[word["word"].lower()+"/"+word["pos"]]=vocabulary_t2[word["word"].lower()+"/"+word["pos"]]+1
				else:
					vocabulary_t2[word["word"].lower()+"/"+word["pos"]]=1
			a_t2=a_t2+1		
		except:
			print("n")
idf={}
for id, object in vocabulary_t2.items():
	idf[id.split("/")[0]]=[math.log(a_t2/object,10),id.split("/")[1]]
vec_name=sorted(idf,key=idf.__getitem__,reverse=True)[1:300]

with open("task_2.txt","w") as file:
	for id, object in idf.items():
		file.write(id+'|')
	file.write('\n')
	for id, object in idf.items():
		file.write(object[1]+'|')
	file.write('\n')
	for id, object in idf.items():
		file.write(str(object[0])+',')
	file.write('\n')


def tfidf(toke_result,vect):
	cal_tf={}
	cal_tfidf={}
	for vec in vect:
		cal_tf[vec]=0
		for word in toke_result[0]["tokens"]:
			if(vec in word["word"]):
				cal_tf[vec]=cal_tf[vec]+1
	for id,object in cal_tf.items() :
		cal_tfidf[id]=object*idf[id][0]
	return cal_tfidf

file=open("task_2.txt","a")
[5393,22504,98909,102483,111205,132144,184234,239532,256100,286697]
res=tfidf(data2["286697"],vec_name)
for id,object in res.items():
	file.write(str(object)+',')
file.write("\n")
file.close()

#task 3 