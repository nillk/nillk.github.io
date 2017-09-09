---
title: Programming for everybody (Python) - 8.Lists
date: 2015-08-31 01:21:16
categories:
  - programming
  - python
tags:
  - python
  - programming
  - coursera
  - programming for everybody
---

## 8. Lists
### A List is a kind of Collection
A collection allows us to put many values in a **single variable**  
우리가 많은 values 들을 하나의 편리한 가방 안에 넣을 수 있기 때문에 좋아!

### What is not a "Collection"
대부분의 variables은 하나의 값을 가지지. 만약 우리가 새로운 값을 variable 안에 넣으면 오래된 값은 지워지고 새로운 값을 덮어쓰게 됨

### List Constants
List constants는 `[]` (square brakets) 으로 싸여있음. 그리고 내부에 있는 elements들은 `,` (comma) 로 구분됨. list 의 elements는 Python object 의 무엇이든 될 수 있다. 심지어 또 다른 list일지라도. 그리고 당연히 list는 비어있을 수도 있지.

### We already use lists!
```python
for i in [5, 4, 3, 2, 1]:
```
얘 list였잖아

### Looking Inside Lists
string 처럼 우리는 single element를 index를 이용해 얻을 수 있어. `[]`얘를 이용해서.
```python
>>> friends = ['Joseph', 'Glenn', 'Sally']
>>> friends[1]
Glenn
```

### Lists are Mutable
* Strings are **immutable** - 바꿀 수 없다. 그냥 새로운 string을 만드는거지.
* Lists are **mutable** - element를 index를 이용해 바꿀 수 있다.

```python
>>> fruit = 'Banana'
>>> fruit[0] = 'b'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> lotto = [2, 14, 26, 41, 63]
>>> lotto[2] = 28
>>> print lotto
[2, 14, 28, 41, 63]
```

### How long is a list?
```python
>>> len([1, 2, 3, 4])
4
```

list를 parameter로 취해서 list안에 있는 element 의 갯수를 return. any set or sequence와 마찬가지.

### Using the range function
숫자의 list를 되돌려줌. 0부터 paramter 숫자 - 1 까지
```python
>>> range(4)
[0, 1, 2, 3]
```

### A tale of two loops...
```python
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends :
  print 'Happy New Year', friend
```

```python
for i in range(len(friends)):
  friend = frieds[i]
  print 'Happy New Year', friend
```
얘네 두개는 같은 loop

### Concatenating lists using `+`
두개의 list를 adding 해서 새로운 list를 만들 수 있음. original을 수정하진 않음.
```python
>>> a = [1, 2, 3]
>>> b = [4, 5, 6]
>>> c = a + b
>>> print c
[1, 2, 3, 4, 5, 6]
>>> print a
[1, 2, 3]
```

### Lists can be sliced using `:`
List의 조작? 은 String 과 굉장히 비슷해. for나 concatenation이나 slicing이나. String과 같이 second number는 *up to but not including*
```python
>>> t = [9, 41, 12, 3, 74, 15]
>>> t[1:3]
[41, 12]
```

### List Methods
```python
>>> x = list()
>>> type(x)
<type 'list'>
>>> dir(x)
['append', 'count', 'extend', ...]
```

### Building a list from scratch
일단 empty list를 만든 다음에 element를 붙일 수 있음. append! list의 순서는 그대로이고, 제일 마지막에 새 element가 붙음. 한 list 안에 있는 element들의 type이 같을 필요는 없음. `list()` or `[]` 둘 다 empty list

### Is Something is a List?
Python은 list안에 item이 있는지 없는지를 체크하는 두 개의 operator를 제공(`in`, `not in`). True 나 False를 return함. list를 modify는 하지 않음.
```python
>>> some = [1, 9, 21, 10, 16]
>>> 9 in some
True
>>> 20 not in some
True
```

### A list is an ordered sequence
a list can be sorted (i.e. change its order)

```python
>>> friends = ['Joseph', 'Glenn', 'Sally']
>>> friends.sort() # sort yourself
>>> print friends
['Glenn', 'Joseph', 'Sally']
```

### Built in Functions and Lists
`len`, `max`, `min`, `sum`...

### Averaging with a list
1. total, count따로 해서 마지막에 계산하든가
2. list에 몽땅 넣고 마지막에 sum, len function사용하든가
뭐, 같은 접근이지.

### Best Friends: Strings and Lists
Split breaks a string into parts produces a list of strings.
```python
>>> abc = 'With three words'
>>> stuff = abc.split()
>>> print stuff
['With', 'three', 'words']
```

delimiter를 지정할 수도 있음
```python
>>> line = 'first,second;third'
>>> line.split()
['first;second;third']
>>> line.split(';')
['first','second','third']
```

### The Double split pattern
일단 split 한 다음에 하나를 잡아서 걔를 다시 split
```python
words = line.split()
email = words[1]
pieces = email.splie('@')
```

---
### Homework
* [8.4](8.4.py)
* [8.5](8.5.py)
