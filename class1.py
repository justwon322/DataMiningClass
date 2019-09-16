#linear search
def sequential_Search(alist,key_value):
    is_match = False
    for x in range(len(alist)):
        list_value = alist[x]
        condition = list_value == key_value
        if condition:
            print("True", x)
            is_match = True
    if not is_match:
        print("False", -1)

sequential_Search([11,23,58,31,56,77,43,12,65,19],99) # false
sequential_Search([11,23,58,31,56,77,43,12,65,19],19) # true

#binary search
def binary_search(alist,key_value):
    pl = 0
    pr = 0
    if len(alist)>0:
        pr = len(alist) - 1
    pc = pr//2
    a = alist
    for x in range(len(a)):
        if a[pc] > key_value: #배열의 값이 검색조건 보다 크면 오른쪽만
            pl = pc + 1
            pc = pl+pr // 2
            a = alist[pl:pr]
        elif a[pc] < key_value: #배열의 값이 검색조건 보다 작으면 왼쪽만
            pr = pc - 1
            pc = pl+pr // 2
            a = alist[pl:pr]
        elif a[pc] == key_value: #찾음
            print("True",pc)
            break;
        else: #없음
            print("False",pc)
            break;


binary_search([1,2,3,5,8],1) # false
#binary_search([1,2,3,5,8],5) # true
#binary_search([1,2,3,5,8],6) # false

