#1 작은 따옴표에서 escape 할떄 \를 사용가능
print('spam eggs')
print('doesn\'t')
print("doesn't")

#2 재미난건.. 문자열을 * 연산자로 반복가능한다는거..자바도 되는거????
print(3*'un' + 'ium')

#3 문자열을 이을수 있다는건데...변수나 표현식에는 해당되지 않음.
text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)

prefix = 'Py'
print(prefix+'thon')

#4 가장마음에 드는건데, char형태로 형변환없이 사용가능한다는거
word = 'Python'
print(word[0])
print(word[-1])

#5 슬라이싱인데 조금 헷갈린다..
print(word[0:2])
print(word[-2:])

print(len(word))
print(word.format())
