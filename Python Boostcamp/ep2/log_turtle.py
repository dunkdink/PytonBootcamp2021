Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> improt turtle
SyntaxError: invalid syntax
>>> import turtle
>>> t = turtle.Turtle()
>>> t.shape('turtle')
>>> t.forward(100)
>>> t.left(90)
>>> t.forward(100)
>>> t.left(90)
>>> t.forward(100)
>>> t.left(90)
>>> t.forward(100)
>>> t.left(90)
>>> t.reset()
>>> for i in range(4):
	t.forward(100)
	t.left(90)

	
>>> range(4)
range(0, 4)
>>> list(range(4))
[0, 1, 2, 3]
>>> for i in range(5):
	print(i)

	
0
1
2
3
4
>>> for i in [10,50,90]:
	print(i)

	
10
50
90
>>> tao.reset()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    tao.reset()
NameError: name 'tao' is not defined
>>> t.reset()
>>> for i in range(4):
	t.forward(100)
	t.left(90)
	print(i)

	
0
1
2
3
>>> for i in range(4):
	t.forward(100)
	t.left(90)
	print('No.',i)

	
No. 0
No. 1
No. 2
No. 3
>>> for i in range(8):
	t.forward(100)
	t.left(45)
	print('No.',i)

	
No. 0
No. 1
No. 2
No. 3
No. 4
No. 5
No. 6
No. 7
>>> t.reset()
>>> for i in range(8):
	t.forward(100)
	t.left(45)
	print('No.',i)

	
No. 0
No. 1
No. 2
No. 3
No. 4
No. 5
No. 6
No. 7
>>> for i in range(4):
	for i in range(8):
		t.forward(100):
			
SyntaxError: invalid syntax
>>> for i in range(4):
	for i in range(8):
		t.forward(100)
		t.left(45)

		
>>> for i in range(4):
	for j in range(8):
		t.forward(100)
		t.left(45)
	print('8 เหลี่ยม',j)
	t.left(90)

	
8 เหลี่ยม 7
8 เหลี่ยม 7
8 เหลี่ยม 7
8 เหลี่ยม 7
>>> for i in range(4):
	for j in range(8):
		t.forward(100)
		t.left(45)
	print('8 เหลี่ยม',j)
	t.left(90)

	
8 เหลี่ยม 7
8 เหลี่ยม 7
8 เหลี่ยม 7
8 เหลี่ยม 7
>>> t.reset()
>>> for i in range(4):
	for j in range(8):
		t.forward(100)
		t.left(45)
	print('8 เหลี่ยม',i)
	t.left(180)

	
8 เหลี่ยม 0
8 เหลี่ยม 1
8 เหลี่ยม 2
8 เหลี่ยม 3
>>> for i in range(4):
	for j in range(8):
		t.forward(100)
		t.left(45)
	print('8 เหลี่ยม',i)
	t.left(135)

	
8 เหลี่ยม 0
8 เหลี่ยม 1
8 เหลี่ยม 2
8 เหลี่ยม 3
>>> t.reset()
>>> for i in range(4):
	for j in range(8):
		t.forward(100)
		t.left(45)
	print('8 เหลี่ยม',i)
	t.left(135)

	
8 เหลี่ยม 0
8 เหลี่ยม 1
8 เหลี่ยม 2
8 เหลี่ยม 3
>>> for i in range(10):
	for j in range(8):
		t.forward(100)
		t.left(45)
	print('8 เหลี่ยม',i)
	t.left(36)

	
8 เหลี่ยม 0
8 เหลี่ยม 1
8 เหลี่ยม 2
8 เหลี่ยม 3
8 เหลี่ยม 4
8 เหลี่ยม 5
8 เหลี่ยม 6
8 เหลี่ยม 7
8 เหลี่ยม 8
8 เหลี่ยม 9


>>> t.reset()
>>> def regtangle():
	for i in range(4):
		t.forward(100)
		t.left(90)

		
>>> regtangle()
>>> for i in range(10)
SyntaxError: invalid syntax
>>> for i in range(10):
	regtangle()
	tao.left(36)

	
Traceback (most recent call last):
  File "<pyshell#70>", line 3, in <module>
    tao.left(36)
NameError: name 'tao' is not defined
>>> for i in range(10):
	regtangle()
	t.left(36)

	
>>> t.reset
<bound method RawTurtle.reset of <turtle.Turtle object at 0x000001DBA960A430>>
>>> t.reset()
>>> 