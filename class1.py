#linear search
###########################
# 1. 선형검색
#   - 검색의 대상이 되는 list와 찾을 값을 각각 alist,key_value로 입력 받는 함수
#   - 결과값으로 입력리스트에 검색값이 있으면 "True"와 n번째 인덱스를 출력하고
#     없으면 "False -1" 을 출력
###########################
def sequential_Search(alist,key_value):
    is_match = False #리스트에 검색 값이 있는지 여부 기본 false
    for x in range(len(alist)): #alist의 길이 만큼 반복하면서 순차적으로 검색하기위한 반복문 선언
        list_value = alist[x] #alist의 n번째 값을 따로 변수에 저장
        condition = list_value == key_value #저장한 리스트 n번째 값을 검색 조건과 비교하여 일치여부 판단후, condition에 저장
        if condition:
            print("True", x) #검색조건과 일치시, True와 몇번째 인덱스 인지 출력
            is_match = True #검색값을 찾았으므로, True 변경
            break #더이상 의미가 없으므로 반복문 강제종료
    if not is_match: #만약 검색값을 찾지 못했다면 is_match = False 이므로, 아래코드가 실행되어 찾지 못하였다고 출력
        print("False", -1)

sequential_Search([11,23,58,31,56,77,43,12,65,19],99) # false
sequential_Search([11,23,58,31,56,77,43,12,65,19],19) # true

#binary search
###########################
# 1. 이진검색
#   - 검색의 대상이 되는 list와 찾을 값을 각각 alist,key_value로 입력 받는 함수
#   - 결과값으로 입력리스트에 검색값이 있으면 "True"와 n번째 인덱스를 출력하고
#     없으면 "False -1" 을 출력
#   - 결과값으로 인덱스를 찾아야 하므로 wrapper 함수와 실제 실행함수 2개로 작성
###########################
def binary_wrapper(alist,key_value):
    binary_search(alist,key_value,0)#사용자는 2가지값만 입력 하므로, wrapper함수에서 index값을 0으로 초기화하여 실행


def binary_search(alist,key_value,index):
    # index는, 재귀호출을 통하여 리스트를 자르고 다시 생성하므로, 원래 리스트의 인덱스를 찾기 위하여 사용하는 변수
    pl = 0 #왼쪽 index(재귀 호출 하므로 항상 0)
    if len(alist) > 0: #길이가 0보다 작거나 같다면, 리스트를 더이상 쪼갤수 없다는것이고 이는 검색값을 찾지 못한 것이므로 함수 종료처리
        pr = len(alist) - 1 #오른쪽 index
        pc = pr // 2 #중간 index
    else:
        print("False -1")
        return #검색값을 찾지 못하면 "False -1"출력 후 함수 실행 종료

    mid_value = alist[pc] #가운데 값 저장
    if mid_value < key_value: #검색조건값이 리스트의 중간 값 보다 크면 중간 값의 오른쪽만 남기고 버림
        pl = pc + 1 #중간값의 다음값 부터 리스트를 재생성 하기위하여
        pc = (pl + pr) // 2 #원래 리스트의 인덱스 값을 위한 pc 재생성
        index = index + pc #계속 중간인덱스을 자기자신에 더하면서 리스트가 재 생성되더라도 원래 리스트의 인덱스 값을 항상 저장하고있음
        binary_search(alist[pl:pr+1], key_value,index) #배열 재생성 후 재귀호출
    elif mid_value > key_value: #검색조건값이 리스트의 중간 값 보다 작으면 중간 값의 왼쪽만 남기고 버림
        pr = pc - 1 #중간값의 이전값 부터 리스트를 재생성 하기위하여
        pc = (pl + pr) // 2 #원래 리스트의 인덱스 값을 위한 pc 재생성
        index = index + pc #계속 중간인덱스를 자기자신에 더하면서 리스트가 재 생성되더라도 원래 리스트의 인덱스 값을 항상 저장하고있음
        binary_search(alist[pl:pr+1], key_value,index) #배열 재생성 후 재귀호출
    elif mid_value == key_value: #중간값과 검색값이 같다면 프로그램 종료
        print("True",index)

binary_wrapper([1,2,3,5,8],4) # false
binary_wrapper([1,2,3,5,8],5) # true

#bubble sort
###########################
# 1. 버블정렬
#   - 리스트를 받으면 작은값부터 왼쪽으로 정렬하여 리스트 반환
###########################
def bubble_sort(alist):
    list_len = len(alist) - 1 #리스트 길이
    for x in range(list_len,0,-1): #오른쪽부터 값 확인하여 정렬 하므로 큰값부터 작아지도록 리스트 길이부터 1까지 -1씩 작아지며 반복수행
        for y in range(x-1,-1,-1): #n-1회 패스 수행 해야 하므로 x-1
            if alist[y] > alist[y + 1]: #대소 비교 후 값 서로 값 바꿔줌
                temp = alist[y +1]
                alist[y + 1] = alist[y]
                alist[y] = temp
    return alist #모든 반복문이 종료되면 리스트 반환

print(bubble_sort([14,46,43,27,0,41,45,91,70]))
print(bubble_sort([14,46,43,27,57,41,45,21,70]))

