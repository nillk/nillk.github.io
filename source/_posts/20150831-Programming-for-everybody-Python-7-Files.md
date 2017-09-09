---
title: Programming for everybody (Python) - 7.Files
date: 2015-08-31 01:19:16
categories:
  - programming
  - python
tags:
  - python
  - programming
  - coursera
  - programming for everybody
---

## 7. Files
그동안 우리가 한 건 그냥 정말 python이랑 논 거. 그냥 **CPU**랑 **Main Memory**사이를 왔다갔다 하면서. 절대 여길 떠나지 않았지! 그래서 이젠 **Secondary Memory**를 사용해보려고 해! *permanent media!* 우리는 python을 이용해서 파일을 쓰거나 읽을 수 있지!

### File Processing
텍스트 파일은 *sequence of lines*라고 볼 수 있지

### Opening a File
일단 `open()` function을 사용해서 Python에게 우리가 어떤 파일을 읽을건지 말해줘야 한다. `open()` 은 **file handle** 을 return해! 뭐 그냥 file 관련 동작을 수행할 수 있는 variable?
어떻게 보면 보통의 프로그램에서 수행하는 **[File > Open]** 동작이랑 비슷하다고 보면 됨!

### Using open()
built-in function in Python
```python
handle = open(filename, mode)
```
- return a handle use to manipulate the file
- filename is a string
- mode is optional and should be 'r' if we are planning reading the file and 'w' if we are going to write to the file

### What is a Handle?
```python
fhand = open('mbox.txt')
print fhand
<open file 'mbox.txt', mode 'r' at 0x1005088b0>
```

### When Files are Missing
Traceback을 보게 되겠지. IOError NO such file or directory!

### The newline Character
special charater in files. 라인의 끝을 가리킴 => `'\n'` => 얘는 여전히 one charater다!
```python
>>> stuff = 'Hello\nWorld!'
>>> stuff
'Hello\nWorld!'
>>> print stuff
Hello
World!
```

### File Processing
A text file can be thought of as a sequence of lines  
각각의 라인 끝에는 `\n` character가 있겠지!

### File Handle as a Sequence
파일은 sequence of lines라고 했지. sequence는 for로 interative하게 사용할 수 있어. sequence는 ordered set이라는 걸 기억해라!
```python
xfile = open('mbox.txt')
for cheese in xfile:
  print cheese
```

### Counting Lines in a File
```python
fhand = open('mbox.txt')
count = 0
for line in fhand:
  count = count + 1
print 'Line Count: ', count
```

### Reading the Whole File
큰 파일은 당연히 힘들겠지만, 작은 건 괜춘!
```python
fhand = open('mbox-short.txt')
inp = fhand.read()
print len(inp)
```
전체 파일의 character 수를 알려줌

### Searching Through a File
```python
fhand = open('mbox-short.txt')
for line in fhand:
  if line.startswith('Form:'):
    print line
```
BUT! 이렇게 하면 문제가 생겨! 아마 중간에 빈 줄이 하나씩 나올거야! 왜일까?  
원래 문장에는 `\n`(newline character)가 있었겠지. 그리고 print는 *newline character를 각각의 line에 더한다.* 그러니 그게 중복이 돼서 빈 줄이 하나씩 나오는 것.

### Searching Through a File (fixed)
그렇다면 문자열에서 오른쪽에 붙는 whitespace를 잘라버리면 간단하다. `rstrip()`
```python
fhand = open('mbox-short.txt')
for line in fhand:
  line = line.rstrip()
  if line.startswith('Form:'):
    print line
```

### Skipping with continue
```python
fhand = open('mbox-short.txt')
for line in fhand:
  line = line.rstrip()
  # Skip 'unintersting line'
  if not line.startswith('From:'):
    continue
  print line
```

### Using in to select lines
```python
fhand = open('mbox-short.txt')
for line in fhand:
  line = line.rstrip()
  if not '@uct.ac.za' in line:
    continue
  print line
```

### Prompt for File Name
```python
fname = raw_input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
  if line.startswith('Subject:'):
    count = count + 1
print 'There were ', count, 'subject lines in', fname
```

### Bad File Names
`try` & `except` 구문을 이용해 이상한 파일명이 들어와서 프로그램이 멈추는 걸 방지하자!
```python
frame = raw_input('Enter the file name:')
try:
  fhand = open(fname)
except:
  print 'File cannot be opened:', fname
  exit()
count = 0
for line in fhand:
  if line.startswith('Subject:'):
    count = count + 1
print 'There were ', count, 'subject lines in', frame
```

---
### Homework
* [7.1](7.1.py)
* [7.2](7.2.py)
* [mbox-short](mbox-short.txt)
