---
title: Programming for everybody (Python) - 2.Expressions, Types
date: 2015-08-31 01:10:16
categories:
  - programming
  - python
tags:
  - python
  - programming
  - coursera
  - programming for everybody
---

## 2.1 Expressions

### Constants And Variable
- Constants : 숫자, 문자, 문자열 등 고정된 값. 안 바뀜. 문자열은 ‘나 “둘 다 쓸 수 있음
- Variables : 컴퓨터의 메모리에 저장할 수 있는 애. 우리는 이름으로 얘네를 가져다 쓸 수 있음. 그리고 물론, Constants와 다르게 얘네 값을 바꿀 수 있지.

### Naming Rules
- 문자나 _ 로 시작
- 문자, 숫자, _ 허용
- Case sensitive

### Reserved Words
-


### Sentences or Lines
```
x = 2
```
Assignment Statement : assign a value to a variable

```
x = x + 2
```
Assignment with expression : right side is an expression, after calculate the value and then assign the value to in memory named x variable
```
print x
```
Print statement

### Numeric Expressions
* \+  : Addition
* \-  : Subtraction
* \*  : Multiplication
* /  : Division
* ** : Power
* %  : remainder

### Order of Evaluation
- Python must know which one to do first
- This is called "operator precedence"
- Parenthesis -> Power -> Multiplication, Division and Remainder -> Addition and Subtraction -> Left to Right

##### 많은 사람들이 python3를 배우고 가르치고 사용하려고 하는 시기임. 하지만 실제 아직 Python2로 제작되어 있는 것들이 많기 때문에 천천이 바뀌는 중임.

### Python Integer Division is Weird
2버전에서는 다른 언어들과 동일. 즉 나누기 했을 때 소숫점은 버리고, 대신 int 나누기 float면 소숫점 나오고

## 2.2 Type

Python은 타입을 알 수 있다. 그래서 내가 정말 뭘 의미하는지 알 수 있음
```
>>> 1 + 1
2
>>> 'Hello, ' + 'World!'
'Hello, World!'
```

위 보기와 같이 \+ 기호는 숫자일 때는 더하고 문자열일 때는 이어붙임. 알아서 하는거지. Python이 타입을 알고 있어야 가능한 이야기. But! 그래서 Type은 문제를 일으킬 수도 있지. 기억해, python은 type을 보고 있어. 숫자 + 문자 이런 거 안됨
```
>>> type('Hello')
<type 'str'>
```
type function으로 데이터 type 알 수 있음

### Numbers have two main types
1. Integers
2. Floating Point Numbers

### Type Conversions
When you put an integer and floating point in an expression the integer is implicitly converted to a float

### String Conversions
`int('123')` or `float('123.01')`

### User Input
`raw_input()` : pause and read data from the user. raw_input returns a string

### Comments in Python
\# : single line comment

### String Operations
- \+ : concatenation
- \* : multiple concatenation

### Mnmonic Variable Name
Since we programmers are given a choice in how we choose our variable names, there is a bit of **best practice**  
We name variables to help us remember what we intend to store in them (*mnemonic = memory aid*)  
This can confuse beginning students because well named variable soften **sound** so good that they must be keywords

[http://en.wikipedia.org/wiki/Mnemonic](http://en.wikipedia.org/wiki/Mnemoni)

---
### Homework
* [2.1](2.1.py)
* [2.2](2.2.py)
