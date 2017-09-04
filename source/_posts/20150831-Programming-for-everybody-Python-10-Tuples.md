---
title: Programming for everybody (Python) - 10.Tuples
date: 2015-08-31 01:24:16
categories:
  - programming
  - python
tags:
  - python
  - programming
  - coursera
  - programming for everybody
---

## 10. Tuples
Tuples은 세번째 Collection! List와 Dictionary에 이어서. List랑 비슷함. 순서가 변하지 않고, 0번부터 시작하지.

### But, Tuples are "immutable"
list와 다르게 tuple 은 한 번 생성하면 수정할 수 없어. string 같아
```
>>> x = [9, 8, 7]
>>> x[2] = 6
>>> print (x)
[9, 8, 6]

>>> y = 'ABC'
>>> y[2] = 'D'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment

>>> z = (5, 4, 3)
>>> x[2] = 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

### Thing not to do with tuples
* `sort()`
* `append()`
* `reverse()`
Traceback을 보게 될 것이야

### A Tale of Two Sequences
```
>>> t = tuple()
>>> dir(t)
['count', 'index']
```

### Tuples are more efficient
Python은 tuple을 수정 불가능하게 만들기 때문에 메모리를 사용하는 데 있어 list보다 더 간단하고 더 효과적인 performance 를 낸다. 그래서 우리가 만약에 임시 변수로 뭔가를 사용할 일이 있다면 list보다는 tuple을 쓰는 것이 좋으다.

### Tuples and Assignment
오 우리는 tuple을 할당문의 왼쪽에도 넣을 수 있어!
```
>>> (x, y) = (4, 'fred')
>>> print (y)
fred
>>> (a, b) = (99, 98)
>>> print (a)
99
```

### Tuples and Dictionaries
dictionary의 `items()` 메소드는 (key, value) tuple의 list를 return

### Tuples are Comparable
비교 연산자는 tuples이나 다른 sequence에도 먹힘. 만약 첫번째 item이 같으면 Python은 다음 항목으로 넘어감. 다른 애를 찾을 때까지!
```
>>> (0, 1, 2) < (5, 1, 2)
True
>>> (0, 1, 20000) < (0, 3, 4)
True
>>> ('Jones', 'Sally') < ('Jones', 'Fred')
False
>>> ('Jones', 'Sally') > ('Adams', 'Sam')
True
```

### Sorting Lists of Tuples
우리는 sorting된 dictionary를 원할 때, tuples의 list를 sorting하는 방식을 쓸 수 있어!
```
>>> d = {'a':10, 'b':1, 'c':22}
>>> t = d.items()
>>> t
[('a', 10), ('b', 1), ('c', 22)]
>>> t.sort()
>>> t
[('a', 10), ('b', 1), ('c', 22)]
```

### Using sorted()
위와 같은 동작을 그냥 sorted 함수를 이용해서 할 수도 있음

### Sort by values instead of key
```
tmp.sort(reverse=True)
```

### 10 Most Common Words
```
counts = dict have a count of words
lst = []
for key, value in counts.items():
  lst.append((value, key))

lst.sort(reverse=True)

for value, key in lst[:10]:
  print (key, value)
```

### Even Shorter Version (adv)
```
c = {'a':10, 'b':1, 'c':22}
print (sorted([(v, k) for k, v in c.items()]))
```

---
### Homework
* [10.2](10.2.py)
