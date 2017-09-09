---
title: Programming for everybody (Python) - 4.Functions
date: 2015-08-31 01:14:16
categories:
  - programming
  - python
tags:
  - python
  - programming
  - coursera
  - programming for everybody
---

## 4. Functions
### Stored (and reused) Steps
Functions은 저장해놨다가 다시 쓰고 쓰고 그게 기본적인 idea. 계속해서 사용하게 되는 logic을 저장해두었다가 쉽게 반복해서 불러다 쓰는거지.

### def keyword
python은 def구문을 보면 오! 이건 function이군! 하면서 코드를 기록하기 시작해. indent 블록이 다시 앞으로 나올 때까지(def 구문이 끝날 때까지)
```python
def 함수명():
```
이렇게! 그러면 다음에 계속 함수명() 으로 언제든 불러다 쓸 수 있지!

### Python Function
python에는 두 종류의 function이 있음
1. Built-in functions (Guido wrote this code!!!! HAHA)  
   Python의 일부분으로 제공됨. `raw_input()`, `type()`, `float()`, `int()`...
2. User-defined functions

### Function Definition
function은 arguments(s)를 입력으로 받아서 계산을 하고 결과를 되돌려주는 reusable code임. `def`라는 예약어로 정의함. function은 function명, 괄호, arguments로 불러서 사용할 수 있음.

A function is some stored code that we use. A function takes some input and produces an output.

### Building our Own Functions
`def`예약어로 function을 만들 수 있음. function의 body부분은 indent해야 함. 이렇게 define은 할 수 있지만 execute는 할 수 없지. execute하려면 불러다 써야지. Python은 코드를 읽다가 def 를 읽으면 그 function을 저장하는거지 자동으로 실행하지는 않아.

### Definitions and Uses
우리는 function을 한 번 정의하면 원하는 만큼 불러다 쓸 수 있어. This is the store and reuse pattern

### Arguments
우리가 function을 부를 때 그 function의 input으로 넘기는 값. arguments를 이용함으로써 우리는 function을 부를 때마다 그 값에 따라 function이 다른 일을 하게 할 수 있음. arguments는 parenthesis에 넣는다

### Parameters
function definition에서 쓰는 변수. function 안에서 arguments에 접근할 수 있게 해줌. arguments에 따라 특정한 행동을 할 수 있도록. 그래서 우리는 general-purpose function을 parameter에 따라 다르게 동작하게 쓸 수 있지.

### Return Values
function은 arguments를 받아서 뭔가 계산을 하고 calling expression으로 불리는 어떤 function call의 결과값으로 쓰이는 값 return하지. return statement는 function execution을 끝내고 function의 결과를 return

### Multiple Parameters/Arguments
function definition에 하나 이상의 parameter를 쓸 수 있음. 그럼 그냥 function call할 때 거기에 개수랑 순서가 맞게 argument를 넘겨주면 됨

### Void (non-fruitful) Functions
function이 return값을 안 가지고 있으면 `void` return하는 애들은 `fruitful function`이라고 부름

### To function or not to function
* Organize your code into *paragraphs* - capture a complete thought and *name it*  
* Don't repeat yourself - make it work once and the reuse it  
If something gets too long or complex, break up logical chunks and put those chunks in functions.
* Make a library of common stuff that you do over and over - perhaps share this with your friends

너의 프로그램이 충분히 복잡해지는 순간이 있을거야. 그럼 너는 이렇게 말하게 되겠지!  
Oh, thank heaven for functions!

---
### Homework
* [4.6](4.6.py)