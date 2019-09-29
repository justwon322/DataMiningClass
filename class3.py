#############################
# 실습 2-1
# text5 에서 4개의 문자로 이루어진 단어를 찾고 이 단어들을
# 전체 코퍼스에서의 빈도수를 기준으로 내림차순으로 정리
#############################
from nltk.book import *
import nltk

chat_size4 = [w for w in text5 if len(w) == 4]  # 4개 문자 인 단어만
fdist_size4 = FreqDist(chat_size4)  # 4개 단어의 빈도 계산
chat_list = []  # 출력할 리스트

for w in chat_size4:
    chat_list.append([fdist_size4[w], w])  # 빈도수와 해당단어를 리스트에 저장

chat_list = list(set(map(tuple, chat_list)))  # https://ssoonidev.tistory.com/100 참고함
chat_list.sort(key=lambda x: x[0], reverse=True)  # 정렬, 구글링으로 찾음
# print(chat_list)

##############################
# 실습 2-2
# text6에 있는 모든 단어들 중 다음에 해당하는 단어들을 찾고 리스트로 만
# 들라.
# a. ize 로 끝나는 단어들
# b. z 를 포함하는 단어들
# c. pt 라는 문자열을 포함하는 단어들
##############################
text6_ize = [w for w in text6 if "ize" == w[-3:].lower()]  # 마지막 3글자가 ize인건들을 찾음
text6_z = [w for w in text6 if "z" in w.lower()]  # z가 있으면 리스트에저장
text6_pt = [w for w in text6 if "pt" in w.lower()]  # "pt"가 있으면 리스트에 저장
# print(text6_ize)  # 출력및 확인
# print(text6_z)
# print(text6_pt)


############################
# 실습 2-3
# 주어진 텍스트에서 불용어(stopwords)가 아닌 단어들 중 상위 50개의 단어를 찾아서
# 반환하는 메서드를 작성하고 Brown corpus 의 임의의 카테고리의 문서를 이용하여 메서드를 실행
############################
def exercise3(text):
    stopwords = nltk.corpus.stopwords.words('english')  # 불용어 저장
    target = [w for w in text if w.lower() not in stopwords]  # 불용어가 아닌것들을 리스트에 저장
    fdist_target = FreqDist(target)  # 불용어가 아닌것들의 빈도수 체크
    sorted_list = []  # 이 밑으로는 실습 2-1의 정렬코드를 이용
    for w in target:
        sorted_list.append([fdist_target[w], w])

    sorted_list = list(set(map(tuple, sorted_list)))  # https://ssoonidev.tistory.com/100
    sorted_list.sort(key=lambda x: x[0], reverse=True)
    sorted_list = sorted_list[:50]

    return_list = []  # 단어만 반환 해야 하므로 새로운 리스트생성

    for w in sorted_list:  # 빈도수 뺴고 단어만 추가
        return_list.append(w[1])

    return print(return_list)  # 출력


exercise3(nltk.corpus.nps_chat.words())
