#점프 투 파이썬 + 수업 내용 같이 정리

#LIST 
#리스트 형태: 리스트명 = [요소1, 요소2, 요소3, ...]

#리스트의 인덱싱
a = [1, 2, 3]
a[0] # =1

#리스트의 슬라이싱
a = [1, 2, 3, 4, 5]
a[0:2] # = [1, 2]

#리스트 관련 함수
#append: 리스트 맨 마지막에 새로운 값 추가
arr = ['math', 'biology', 1989, 2019]
arr.append(2021)
print(arr) # = ['math', 'biology', 1989, 2019, 2021]

#sort: 리스트 요소를 순서대로 정렬(리스트의 값 자체의 순서를 정렬)
a = [1, 3, 2, 5, 4]
a.sort()
print(a) # = [1, 2, 3, 4, 5]

#sorted: 리스트 자체의 순서는 유지하고, 정렬된 순서로 출력만 함
b = [1, 3, 2, 5, 4]

print(sorted(b)) # = [1, 2, 3, 4, 5]
print(b) # = [1, 3, 2, 5, 4]

#reverse: 리스트를 역순으로 뒤집음
c = ['a', 'b', 'd', 'c']
c.reverse()
print(c) # =['c', 'd', 'b', 'a']


#insert(): 리스트 중간에 인덱스와 값을 지정하여 값을 추가 삽입
arr_in = ['math', 'biology', 1989, 2019]
arr_in.insert(1, 2021) #인덱스 1 위치에 2021 넣기
print(arr_in) # = ['math', 2021, 'biology', 1989, 2019]

#del: 제거할 항목의 인덱스에 따라 삭제, 삭제된 값은 확인할 수 없음
#del 활용 예시 : 웹사이트에서 특정 사용자가 탈퇴하는 경우, 인덱스를 활용하여 삭제 가능
arr_del = [1, 2, 3, 4, 5]
breakpoint()
del arr_del[3]
print(arr_del) # = [1, 2, 3, 5]

#remove: 리스트 요소 제거, 인덱스가 아니라 삭제할 항목의 값을 알고 있어야 함
arr = [1, 2, 3, 4, 5]
arr.remove(2)
print(arr) #[1, 3, 4, 5]

arr_1 = [1, 2, 3, 4, 5, 1, 1, 1]
arr_1.remove(1)
print(arr_1) #[2, 3, 4, 5, 1, 1, 1] #맨 앞 1만 제거

# pop: 리스트 요소 끄집어내기, 리스트에서 특정 위치의 값을 빼내는 기능
# pop 활용 예시 : 웹에서 로그아웃한 특정 사용자를 빼놨다가, 재접속 및 로그인을 위해서 사용자 목록에 다시 넣을 수 있음
arr_pop = [1, 2, 3, 4, 5, 8, 9, 10]
p_1 = arr_pop.pop()
print(arr_pop) #[1,2,3,4,5,8,9]
print(p_1) #10

p_2 = arr_pop.pop()
print(arr_pop) #[1,2,3,4,5,8]
print(p_2) #9

p_3 = arr_pop.pop(1) #인덱스 1인 숫자만 꺼내기
print(arr_pop) #[1,3,4,5,8]
print(p_3) #2

#extend(): 리스트 확장, 리스트끼리 이어 붙이기
arr_one = [1, 2, 3, 4, 5]
arr_two = [1, 2, 3]
arr_one.extend(arr_two)
print(arr_one)

#sum()
arr = [1, 2, 3, 4, 5]
print(sum(arr)) #15

#count():리스트 안에 특정 값의 갯수 세기
arr = [1, 1, 1, 2, 3]
print(arr.count(1)) #3
print(arr.count(2)) #1
print(arr.count(3)) #1

#len(): 리스트 길이 확인
arr = [1, 2, 3, 4, 5]
print(len(arr)) #5

#index(): 리스트 범위에서 특정 값의 인덱스 반환
arr_two = ['a', 'b', 'c', 'd', 'e', 'a', 'b']
print(arr_two.index('a', 0, 5)) #0 #0번째~5번째 위치에서 a의 위치 찾기
print(arr_two.index('b', 1, 3)) #1 #1번째~3번째 위치에서 b의 위치 찾기

#min(): 최소값 반환
arr = [4, 3, 2.5, 7, 0.7, 9]
print(min(arr)) #0.7


