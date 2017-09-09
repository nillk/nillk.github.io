---
title: Programming for everybody (Python) - 9.Dictionaries
date: 2015-08-31 01:23:16
categories:
  - programming
  - python
tags:
  - python
  - programming
  - coursera
  - programming for everybody
---


## 9. Dictionaries
### What is a Collection?
Collection은 일종의 짐보따리 같은 것. 안에 아무 거나 넣을 수 있는. 우리는 아무거나 넣어서 그걸 아무데나 들고 다닐 수 있어. 일종의 편리한 짐가방처럼.

### What is not a "Collection"
우리가 아는 대부분의 variables은 하나의 값만을 가짐. 만약 우리가 새로운 값을 넣는다면? 오래된 값은 over written되지. list와 dictionary의 차이점은 내부에 값이 어떻게 구성되어 있는가이다.

### A story of Two Collections..
* List  
A linear collection of values that stay in order. 인덱스 별로 들어가 있어 값이. 0, 1, 2, 3... 프링글스같지!
* Dictionary  
A **bag** of values, each with its own label. 순서 없이 큰 값 작은 값 뭐든 가지고 있다. 그리고 각각의 것들은 label을 가지고 있음. key/value 라고 부른다. key는 label이고 value는 뭐든 상관 없음. 우리는 key로 value를 얻을 수 있다.

### Dictionaries
python의 가장 강력한 data collection. 빠른 db 와 같은 일을 할 수 있음.
* Perl/php - Associative Arrays
* Java - Properties or Map or HashMap
* C#/.Net - Property Bag
다른 언어에서는 이렇게 다른 이름들을 가지고 있지. 쟤네도 Dictionary야

List는 가지고 있는 값들의 list내의 위치를 기반으로 index. Dictionaries는 가방이다. 순서가 없음. 그래서 우리는 *lookup tag*같은 걸로 우리가 뭘 넣었는지 정리하지.
```python
>>> purse = dict()
>>> purse['money'] = 12
>>> purse['candy'] = 3
>>> print purse
{'money':12, 'candy':3}
>>> print purse['candy']
3
>>> purse['candy'] = purse['candy'] + 2
>>> print purse
{'money':12, 'candy':5}
```

### Comparing Lists and Dictionaries
Dictionaries는 index대신 key를 값을 얻기 위해 사용한다는 점만 다름. List는 순서유지 Dictionaries는 유지 X

### Dictionary Literals (Constants)
Dictionary literals 는 `{}` 얘를 씀. key : value pair로. 그냥 `{}`만 써서 빈 dictionary를 만들 수도 있음
```python
jjj = {'chunk':1, 'fred':42, 'jan':100}
```

### Many Counters with a Dictionary
Dictionary를 쓰는 일반적인 이유 중 하나는 *세는*일이다. counting

### Dictionary Tracebacks
key가 dict안에 없는데 참조하려고 하면 에러남! 그래서 우리는 in 을 사용해서 이 키 값이 dictionary안에 있는지 없는지 확인할 수 있다.
```python
print 'csev' in ccc
```

### When we see a new name
만약 새로운 key가 나타나면 새로 추가해야겠지! 아니면 그냥 원래 있던 값을 쓰면 되고!

### The get method for dictionary
`get`메소드를 이용해 키 값이 없는 경우의 기본값을 지정할 수 있음
```python
counts.get(name, 0)
```
name키가 존재하는 경우 값을 리턴 아니면 0

### Simplified counting with get()
```python
counts[name] = counts.get(name, 0) + 1
```
걍 이러면 됨!

### Counting Pattern
일반적으로 한 라인에 있는 단어의 수를 세기 위해서는 일단 split! 그다음에 loop를 돌면서 dictionary를 이용해 counting

### Definite Loops and Dictionaries
Dictionary는 순서대로 저장되어 있지는 않지만 그냥 for 문을 써서 모든 entries 를 읽을 수는 있어.

### Retrieving lists of Keys and Values
```python
>>> jjj = {'chunk':1, 'fred':42, 'jan':100}
>>> jjj.keys()
['jan', 'chunk', 'fred']
>>> jjj.values()
[100, 1, 42]
>>> jjj.items()
[('jan', 100), ('chunk'1), ('fred', 42)]
```

### Bonus : Two Iteration Variables!
우리는 dictionary에서 loop를 돌면서 2개의 iteration variables를 가질 수 있음. 첫번째 variable은 key, 두번째 variable은 value
```python
for key, value in jjj.items():
  print key, value
```

---
### Homework
* [9.4](9.4.py)