# this is the frist comment
spam = 1 # and this is the second comment
         # ... and now a third!
text = "# This is not a comment because it's inside quotes."


width = 20
height = 5*9
print (width * height)

s = 'First line. \nSecond line.'
print ('"Isn\'t", they said.')
print (s)

print ("""\
Usage: thingy [OPTIONS]
    -h
    -H hostname
""")

s = 3*'un'+'ium'
print(s)

s = 'Py'
print (s+'thon')

# text indexing...
ss = s+'thon'
print (ss[0])
print (ss[-1])

# text slicing...
# 슬라이싱(slicing)은 부분 문자열(substring)을 얻는 데 사용
print (ss[0:2])
print (ss[2:5])
print (ss[:2])
print (ss[4:])
print (ss[-2:])
print (ss[:2]+ss[2:])

# 리스트(list)
squares = [1, 4, 9, 16,25]
print (squares)
print (squares[0])
print (squares[-1])
print (squares[-3:])
print (squares[:])
are = squares + [36, 49, 64, 81, 100]
print (are)

cubes = [1,8,27,65,125]
print(cubes)
print(4**3)
cubes[3] = [7,75,77]
print(cubes[3])
print (cubes)
print (cubes[3][2])
cubes.append(216)
cubes.append(7**3)
print (cubes)