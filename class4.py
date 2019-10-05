from bs4 import BeautifulSoup
import re
import os
import string
from nltk.stem import PorterStemmer

doc = ""
for line in open('./data/cranfieldDocs/cranfield0001', 'r'):
    doc += line


cleantext = BeautifulSoup(doc,"lxml").text
lowertext = cleantext.lower()

lowertext = ''.join(i for i in lowertext if not i.isdigit())
#join 은 리스트 형태를 string 형태로 바꿔줌
#if not digit 이므로 숫자가 아닌것만 lowertext에 저장

tokenedtext = re.findall(r"[\w']+|[.,!?;]",lowertext)
#\w = 문자 \w' 는 e.g uncle's 에서 's 까지 포함하여 한단어로 인식한다는 뜻이고
#+|[.,!?;] 는 그뒤에 저 [] 안에 문자들 포함하여 토크나이징 하는데, 다른 단어로 인식하여 분리하여 인식함함
print(tokenedtext)

lowertext = ''.join(i for i in lowertext if not i.isdigit())
lowertext = re.sub('\W+',' ',lowertext)
tokenedtext = lowertext.split()

lowertext = ''.join(i for i in lowertext if not i.isdigit())
tokenedtext = lowertext.split()
tokenedtext2 = [x for x in tokenedtext if x not in string.punctuation]
#문장 부호 삭제


stopWords = []
for line in open('./data/stopwords_nltk.txt'):
    stopWords.append(line.split()[0]) #whitespace를 기준으로 나눠서 \n(줄바꿈) 문자 뺴고 단어만 리스트에 저장

tokenedtext3 = [x for x in tokenedtext2 if x not in stopWords]

ps = PorterStemmer()
stemmedtext = [ps.stem(x) for x in tokenedtext3]
print(stemmedtext)
#ps.stem(x) 는 x의 어간만 추출한다.
#추출하여 stemmedtext list에 저장

dir = './data/cranfieldDocs/'
filenames = os.listdir(dir)
print(filenames)

for filename in os.listdir(dir):
    docpath = (os.path.join(dir,filename))
    print(docpath)

