#1 정적이 아닌 동적으로 가변적으로 내용을 변경하거나 추가할수 있다
squares = [1, 4, 9, 16, 25]
print(squares)
print(squares[0:1])

#2 '+='도 되넹..
squares += [36, 49, 64, 81, 100]
print(squares)

squares[0] = 'test'
print(squares)

#3 값 삭제시 '[]' 으로
squares[0:2] = []
print(squares)

#4 삭제 이후 인덱스도 변경된당.
print(squares[0])

#5 '' or ""은 빈값으로 인식을 안한다
squares[0] = ""
print(squares)

#6 리스트를 중첩할수 있다..자바야 반성하자
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)