from nltk.book import *
import nltk

chat_size4 = [w for w in text5 if len(w) == 4]  # 4개 문자 인 단어만
fdist_size4 = FreqDist(chat_size4)  # 4개 단어의 빈도 계산
chat_list = []  #

for w in chat_size4:
    chat_list.append([fdist_size4[w], w])

chat_list = list(set(map(tuple, chat_list)))  # https://ssoonidev.tistory.com/100 참고함
chat_list.sort(key=lambda x: x[0], reverse=True)
# print(chat_list)

text6_ize = [w.lower() for w in text6 if "ize" == w[-3:].lower()]
text6_z = [w.lower() for w in text6 if "z" in w]
text6_pt = [w.lower() for w in text6 if "pt" in w]


# print(text6_ize)
# print(text6_z)
# print(text6_pt)

def unusual_words(text):
    text_vocab = set(w.lower() for w in text if w.isalpha())
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    unsual = text_vocab - english_vocab
    return sorted(unsual)


def quiz3(text):
    stopwords = nltk.corpus.stopwords.words('english')
    target = [w for w in text if w.lower() not in stopwords]
    fdist_target = FreqDist(target)
    sorted_list = []
    for w in target:
        sorted_list.append([fdist_target[w], w])

    sorted_list = list(set(map(tuple, sorted_list)))  # https://ssoonidev.tistory.com/100
    sorted_list.sort(key=lambda x: x[0], reverse=True)
    sorted_list = sorted_list[:50]

    return_list = []

    for w in sorted_list:
        return_list.append(w[1])

    return print(return_list)


quiz3(nltk.corpus.nps_chat.words())
# print(unusual_words(nltk.corpus.nps_chat.words()))
