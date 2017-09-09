---
title: Programming for everybody (Python) - 5.Loop
date: 2015-08-31 01:16:16
categories:
  - programming
  - python
tags:
  - python
  - programming
  - coursera
  - programming for everybody
---

## 5. Loop
### Repeated Steps
while이 if와 다른 점은 condition을 만족하는 한 indent된 구문을 계속해서 다시 실행한다는 것
* iteration variables : some variable that is changing each time through the loop. iteration variable controls how many times the loop runs

### An Infinite Loop
우리는 사실 대부분의 경우 이 무한루프를 원하지 않지. 대부분은 실수야. 무한루프는 절대 끝나지 않는다구!

### Another Loop
never run. 단 한 번도 조건을 만족시키지 못한거지. == Zero Loop

### Breaking Out of a Loog
The `break statement` ends the current loop and jumps to the statement immediately following the loop  
조건이 끝나는 것 외에 또 다른 loop를 벗어나는 방법이지!

### Finishing an Interation with continue
The `continue statement` ends the current iteration and jumps to the top of the loop and starts the next iteration  
이번 iteration은 끝났어! loop를 끝내고 싶지는 않지만 이번 iteration은 끝내고 다음 iteration으로 넘어가고 싶어!

### Indefinite Loops
`while` called *indefinite loops* because they keep going until a logical condition becomes False  
가끔 우리는 그래서 이게 끝날지 아닐지 확신할 수 없지.

### Definite Loops
list나 set 같은 것들 finite set. for로 사용할 수 있는 것들. 이것들은 정확한 횟수로 동작하기 때문에 이렇게 불러.  
definite loops iterate through the members of a set

### Loop Idioms What We Do In Loops
How we construct loops  
How we think like a computer

### Making *smart* loops
how to kind of build intelligence into loops

### Looping through a Set
```python
for thing in [9, 41, 12, 3, 74, 15]:
  thing
```
What is the largest number?

### Finding the largest value
```python
largest_so_far = -1
for thing in [9, 41, 12, 3, 74, 15]:
  if thing > largest_so_far:
    largest_so_far = thing
print largest_so_far
```
largest_so_far = 9 -> 41 -> 41 -> 41 -> 74 -> 74 (loop 안에서 변화)

### Counting in a Loop
```python
zork = 0
for thing in [9, 41, 12, 3, 74, 15]:
  zork = zork + 1
  print zork, thing
print zork
```
zork = 1 -> 2 -> 3 -> 4 -> 5 -> 6

### Summing in a Loop
```python
zork = 0
for thing in [9, 41, 12, 3, 74, 15]:
  zork = zork + thing
  print zork, thing
print zork
```
zork = 9 -> 50 -> 62 -> 65 -> 139 -> 154

### Finding the Average in a Loop
```python
count = 0
sum = 0
for thing in [9, 41, 12, 3, 74, 15]:
  count = count + 1
  sum = sum + thing
print count, sum, sum/count
```

### Filtering in a Loop
```python
for thing in [9, 41, 12, 3, 74, 15]:
  if thing > 20:
    print 'Large number', thing
```

### Search Using a Boolean Variable
```python
found = False
for thing in [9, 41, 12, 3, 74, 15]:
  if thing == 3:
    found = True
  print found, value
print found
```
This means : We found it! There is a three!!!

### Finding the largest value & Finding the smallest value
초기값을 어떻게 정하느냐에 따라 값이 이상하게 나올 수 있어. 초기값을 -1로 정하고 loop를 돌았는데 전부 -1보다 크면? 그럼 최소값은 초기값(-1)이 그대로 나올거야. 이건 우리가 원하는 바가 아니지!

### None value
```python
smallest = None
for value in [9, 41, 12, 3, 74, 15]:
  if smallest is None:
    smallest = value
  elif value < smallest:
    smallest = value
print smallest
```

### The `is` and `is not` Operators
Don't start overusing it. It's at a low level its real meaning is exactly the same as in type and value. Similar to, but stronger than ==

---
### Homework
* [5.2](5.2.py)
