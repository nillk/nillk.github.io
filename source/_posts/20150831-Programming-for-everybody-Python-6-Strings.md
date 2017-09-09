---
title: Programming for everybody (Python) - 6.Strings
date: 2015-08-31 01:18:16
categories:
  - programming
  - python
tags:
  - python
  - programming
  - coursera
  - programming for everybody
---

## 6. String
### String Data Type
A string is a sequence of characters.  
A string literal uses quotes `'Hello'` or `"Hello"`  
For strings, `+` means **concatenate**  
When a string contains numbers, it is still a string  
We can convert numbers in a string into a number using `int()`

### Reading and Converting
`raw_input` : 모든 입력을 string으로 받음

### Looking Inside Strings
index와 square brackets을 이용해 string내부의 single character를 얻을 수 있음. index는 0부터 시작하는 int (물론 n-1 같은  expression도 가능)

### A Character Too Far
문자열 길이를 넘어간 index를 넣으면 에러를 받을 것이야!!! 그러니 조심해라

### Len Function
```python
>>> len('banana')
6
```

### Looping Through Strings
1. use while and len function
```python
fruit = 'banana'
index = 0
while index < len(fruit):
```

2. using for
```python
fruit = 'banana'
for letter in fruit:
```
The iteration variable is completely taken care of by the for loop

### Looping and Counting
```python
fruit = 'banana'
count = 0
for letter in fruit:
  if letter == 'a':
    count = count + 1
print count
```

### Looking deepter into in
The iteration variable **iterates** though the sequence (ordered set)  
The block (body) of code is executed once for each value in the sequence  
The iteration variable moves through all of the values in the sequence

### Slicing Strings
We can also look at any continuous section of a string using a colon operator  
The second number is one beyond the end of the slice - *up to but not including*  
If the second number is beyond the end of the string, it stops at the end
```python
>>> s = 'Monty Python'
>>> s[0:4]
'Mont'
>>> s[6:7]
'P'
>>> s[6:20]
'Python'
```

문자 자를 때 첫번째 문자나 마지막 문자를 비워두면 그건 그냥 처음 or 끝이라는 얘기

### String Concatenation
\+ 기호로 두 문자열을 붙일 수 있음

### Using in as an Operator
`in` : String 문자열 안에 어떤 문자열이 들어있는지 확인할 수 있음. logical expression. return True or False
```python
>>> fruit = 'banana'
>>> 'n' in fruit
True
>>> 'm' in fruit
False
>>> 'nan' in fruit
True
```

### String Comparison
```python
if word == 'banana':
if word < 'banana':
elif word > 'banana':
```

### String Library
Python은 string library안에 굉장히 많은 string function을 갖고 있다. 이 function들은 모든 string 안에 이미 *built-in* 되어 있음. 그냥 `invoke`하면 됨. 이 function들은 원래의 string을 수정하지는 않음. 그냥 교체된 *새로운 string*을 return
* `upper()` : 대문자로 바꾼 대체 문자열 return  
* `lower()` : 소문자로 바꾼 대체 문자열 return

```python
>>> stuff = 'Hello World'
>>> type(stuff)
<type 'str'>
>>> dir(stuff) # Python 내장 명령이며, 사용할 수 있는 built-in 함수를 보여줌
['capitalize', 'center', 'count', 'decode', ...]
```

### Searching a String
`find()` 함수를 써서 내가 원하는 서브 스트링이 어떤 특정 문자열에 포함되어 있다면 그 첫번째 index를 얻을 수 있음. 만약 특정 문자열에서 서브 스트링을 찾을 수 없다면 -1을 return.
```python
>>> fruit = 'banana'
>>> pos = fruit.find('na')
2
>>> aa = fruit.find('z')
-1
```

### Search and Replace
워드의 모두 찾아서 바꾸기 기능이라고 보면 됨.
```python
>>> greet = 'Hello Bob'
>>> greet.replace('o', 'X')
'HellX BXb'
>>> greet.replace('Bob', 'Jane')
'Hello Jane'
```
greet는 여전히 그대로 Hello Bob

### Stripping Whitespace
* `lstrip()` : 왼쪽 whitespace 제거
* `rstrip()` : 오른쪽 whitespace 제거
* `strip()`  : 양쪽 whitespace 제거

### Prefixes
이게 어떤 문자열로 시작하니?
```python
>>> line = 'Please have a nice day'
>>> line.startswith('Please')
True
>>> line.startswith('p')
False
```

---
### Homework
* [6.5](6.5.py)